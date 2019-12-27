# Twitch Colours
Webapp that integrates with Twitch for dynamic username colours

## Installation
- The frontend needs to be built then deployed as a static page. Node.js dependencies need to be installed with `npm install` then build the app with `npm run build`.
- Install python requirements with `pip install -r requirements.txt` in `backends`. (Use python 3.6+, venv recommended)

## Configuration
The `backend` django server requires an additional settings file that imports `*` from `settings.py` in order to function. - e.g. `local_settings.py` or `prod_settings.py` This settings file is used by django by passing `--settings=<settings module>` with `python manage.py runserver`

## Running
- The backend relies on `celery` with `redis`, so for all endpoints to work `redis-server` and a `celery` worker must be running on the server. The `celery` worker is started with `celery -A colours worker -l info --autoscale=100,1` (autoscale parameter can be adjusted depending on the expected load)
