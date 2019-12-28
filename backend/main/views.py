import json
import requests
from more_itertools import unique_everseen

from celery.result import AsyncResult
from django.contrib.messages import error
from django.http import JsonResponse
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST
from celery.task.control import revoke
from django.core.serializers import serialize
from django.conf import settings

from .models import CeleryTask, Channel, User
from . import tasks, utils
from .encoders import TimeEncoder


def index(request, **kwargs):
    """Index page"""
    # return render(request, 'main/index.html', {
    #     'client_id': settings.TWITCH_CLIENT_ID,
    #     'redirect_uri': settings.TWITCH_REDIRECT_URI,
    #     'state': settings.TWITCH_STATE,
    #     **kwargs,
    # })
    return redirect(settings.APP_URL)


def is_authenticated(request):
    return JsonResponse({
        'authenticated': request.user.is_authenticated
    })


def get_login_url(request):
    return JsonResponse({
        'clientId': settings.TWITCH_CLIENT_ID,
        'redirectUri': settings.TWITCH_REDIRECT_URI,
        'state': settings.TWITCH_STATE
    })


@login_required
def logout_user(request):
    logout(request)

    return redirect(index)


def verify(request):
    """Twitch authorisation"""
    code = request.GET.get('code')
    scope = request.GET.get('scope')
    state = request.GET.get('state')

    # CSRF Protection
    if state != settings.TWITCH_STATE:
        error(request, 'code error')
        return redirect(index)

    # Error occured in authorisation - user likely did not accept
    if None in (code, scope):
        error(request, 'authorisation error')
        return redirect(index)

    # Send POST request to Twitch to get OAuth token
    resp = requests.post('https://id.twitch.tv/oauth2/token', data={
        'client_id': settings.TWITCH_CLIENT_ID,
        'client_secret': settings.TWITCH_CLIENT_SECRET,
        'code': code,
        'grant_type': 'authorization_code',
        'redirect_uri': settings.TWITCH_REDIRECT_URI,
    })
    if resp.status_code != 200:
        error(request, 'Error in response from Twitch. Please try again')
        return redirect(index)

    access_token = resp.json()['access_token']
    refresh_token = resp.json()['refresh_token']

    # Get information about the recently authorised user
    resp = requests.get('https://api.twitch.tv/helix/users',
                        headers={"Authorization": f"Bearer {access_token}"})
    if resp.status_code != 200:
        error(request, 'Error in response from Twitch. Please try again')
        return redirect(index)

    data = resp.json()['data'][0]

    user, _ = User.objects.update_or_create(id=data['id'], defaults={
        'username': data['login'],
        'display_name': data['display_name'],
        'profile_picture': data['profile_image_url'],
        'access_token': access_token,
        'refresh_token': refresh_token,
    })
  
    if user is not None:
        login(request, user)

    return redirect(index)


@login_required
def get_user_info(request):
    """Get display_name and profile_picture url for user"""
    display_name = request.user.display_name
    profile_picture = request.user.profile_picture
    
    return JsonResponse({
        'result': 'success',
        'data': {
            'display_name': display_name,
            'profile_picture': profile_picture
        }
    })


@login_required
def start(request):
    """Start bot"""
    username = request.user.username
    channels = [c.username for c in request.user.channel_set.all()]

    # Check tasks and cancel already running script before starting new
    stop(request)
    
    # Refresh token because TwitchIO can't tell if the token is expired
    refresh_token(request)
    access_token = request.user.access_token

    bot = tasks.run_bot.delay(f'oauth:{access_token}', username, channels)
    CeleryTask.objects.create(user=request.user, id=bot.id)
    
    return JsonResponse({
        'result': 'success',
    })


@login_required
def stop(request):
    """Stop bot"""
    try:
        task_id = request.user.celerytask.id
    except ObjectDoesNotExist:
        pass
    else:
        revoke(task_id, terminate=True)
        request.user.celerytask.delete()

    return JsonResponse({
        'result': 'success',
    })
    
    
@login_required
def get_status(request):
    # Check if there is a running task for the user
    try:
        task_id = request.user.celerytask.id
        task = AsyncResult(task_id)
        assert task.state == 'PENDING'
    except (ObjectDoesNotExist, AttributeError, AssertionError):
        running = False
    else:
        running = True 
        
    return JsonResponse({
        'running': running
    })


@login_required
def refresh_token(request):
    token = request.user.refresh_token
    
    resp = requests.post('https://id.twitch.tv/oauth2/token', data={
        'grant_type': 'refresh_token',
        'refresh_token': token,
        'client_id': settings.TWITCH_CLIENT_ID,
        'client_secret': settings.TWITCH_CLIENT_SECRET,
    })
    if resp.status_code != 200:
        return JsonResponse({
            'result': 'error',
            'error_message': 'Error in response from Twitch'
        })

    request.user.access_token = resp.json()['access_token']
    request.user.refresh_token = resp.json()['refresh_token']
    request.user.save()

    return JsonResponse({
        'result': 'success',
    })


@login_required
def get_channels(request):
    chans = request.user.channel_set.all().order_by('username')

    return JsonResponse({
        'result': 'success',
        'data': [c.display_name for c in chans]
    })


@login_required
@require_POST
def set_channels(request):
    channels = [c for c in set(json.loads(request.body)['items']) if c]
    if len(channels) > 100:
        return JsonResponse({
            'result': 'error',
            'error_message': 'Too many channels'
        })

    # Get data for given channels from Twitch
    token = request.user.access_token
    resp = requests.get(
        'https://api.twitch.tv/helix/users',
        headers={'Authorization': f'Bearer {token}'},
        params={'login': list(channels)}
    )
    if (resp.status_code == 401
            and 'must-revalidate' in resp.headers['cache-control']):
        # Token expired, refresh then retry
        refresh_token(request)
        return set_channels(request)
    elif resp.status_code != 200:
        return JsonResponse({
            'result': 'error',
            'error_message': 'Error in response from Twitch. '
        })

    # Any invalid channels will not be part of the response from Twitch
    response = resp.json()['data']
    channel_dict = {}
    for data in response:
        channel_dict[data['login']] = {
            'id': data['id'],
            'display_name': data['display_name']
        }

    request.user.channel_set.clear()

    for channel in channels:
        channel = channel.lower()
        try:
            channel, _ = Channel.objects.get_or_create(
                id=channel_dict[channel]['id'], defaults={
                    'username': channel,
                    'display_name': channel_dict[channel]['display_name']
                }
            )
        except KeyError:
            continue
        channel.users.add(request.user)

    return JsonResponse({
        'result': 'success',
        'data': [x['display_name'] for x in channel_dict.values()]
    })
    
    
@login_required
def get_colours(request):
    colours = json.loads(request.user.colours)
    
    return JsonResponse({
        'result': 'success',
        'data': colours
    })


@login_required
@require_POST
def set_colours(request):
    colours = unique_everseen(request.POST.getlist('items'))
    colours = [c for c in colours if utils.is_valid_colour(c)]
    if len(colours) > 100:
        return JsonResponse({
            'result': 'error',
            'error_message': 'Too many colours'
        })

    request.user.colours = json.dumps(colours)
    request.user.save()
    
    return JsonResponse({
        'result': 'success',
        'data': colours
    })


@login_required
def logs(request):
    messages = json.loads(serialize(
        'json',
        request.user.message_set.all().order_by('-time')[:10],
        use_natural_foreign_keys=True,
        cls=TimeEncoder
    ))
    
    return JsonResponse({
        'result': 'success',
        'data': messages
    })