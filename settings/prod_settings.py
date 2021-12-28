from settings.dev_settings import *
import dj_database_url

DATABASES['default']: dj_database_url.config(default=os.getenv('DATABASE_URL'), conn_max_age=600)

import django_heroku
django_heroku.settings(locals())
