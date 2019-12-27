# Twitch Colours
Webapp that integrates with Twitch for dynamic username colours

## Installation
The frontend needs to be built then deployed as a static page. Node.js dependencies need to be installed with `npm install` then build the app with `npm run build`.

## Configuration
The `backend` django server requires an additional settings file that imports `*` from `settings.py` in order to function. - e.g. `local_settings.py` or `prod_settings.py` This settings file is used by django by passing `--settings=<settings module>` with `python manage.py runserver`
