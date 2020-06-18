# Twitch Colours
Webapp that integrates with Twitch for dynamic username colours

This was my first project to use Vue.js or Django (or celery, or a relational database), so I apologise for it possibly being an incoherent mess in places. Previously I relied on JQuery and Flask for my webapps, though my largest Flask project was pretty much just spaghetti code.

I currently have this deployed at [colours.zaxu.xyz](https://colours.zaxu.xyz)

## Dependencies
- Node and Python 3.6+ need to be installed on the system. It's also recommended to use a virtual environment for Python (`python -m venv venv`)
- Dependencies for the frontend app should be installed with `npm install` in the `vueapp` subdirectory
- Dependencies for the backend should be installed with `pip install -r requirements.txt` in the `backends` subdirectory

## Configuration
The `backend` django server requires an additional settings file that imports `*` from `settings.py` in order to function. - e.g. `local_settings.py` or `prod_settings.py` This settings file is used by django by passing `--settings=<settings module>` to `manage.py`

## Running
- The backend relies on `celery` with `redis`, so for all endpoints to work `redis-server` and a `celery` worker must be running on the server. The `celery` worker is started with `celery -A colours worker -l info --autoscale=100,1` (autoscale parameter can be adjusted depending on the expected load)

### Development
- Run Vue frontend app with `npm run serve` in `vueapp`
- Run Django backend with `python manage.py runserver --settings=colours.local_settings` (or wherever else your settings are stored)

The Vue app by default proxies `/api/` to `localhost:8000`. If you're running the Django backend on a port other than 8000, you will have to modify the `target` value for `^/api` under `devServer.proxy` in `vueapp/vue.config.js`

### Production
- An optimised version of the Vue app should be built with `npm run build` in `vueapp` and the `dist` contents placed wherever your files are being served
- For deploying the backend, see Django's [documentation](https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/) on it.
