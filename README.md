# Twitch Colours
Webapp that integrates with Twitch for dynamic username colours

## Configuration
The `backend` django server requires an additional settings file that imports `*` from `settings.py` in order to function. - e.g. `local_settings.py` or `prod_settings.py` This settings file is used by django by passing `--settings=<settings module>` with `python manage.py runserver`
