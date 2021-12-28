from settings.dev_settings import *
import dj_database_url
import django_heroku

db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)

django_heroku.settings(locals())
