from settings.dev_settings import *
import dj_database_url

DATABASES['default'] =  dj_database_url.config()


import django_heroku
django_heroku.settings(locals())