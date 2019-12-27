from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('is_authenticated', views.is_authenticated),
    path('get_login_url', views.get_login_url),
    path('verify', views.verify),
    path('logout', views.logout_user),
    path('start', views.start),
    path('stop', views.stop),
    path('refresh_token', views.refresh_token),
    path('get_user_info', views.get_user_info),
    path('get_status', views.get_status),
    path('get_channels', views.get_channels),
    path('set_channels', views.set_channels),
    path('get_colours', views.get_colours),
    path('set_colours', views.set_colours),
    path('get_logs', views.logs),
]
