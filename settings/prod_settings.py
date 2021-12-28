from settings.dev_settings import *
import dj_database_url


import django_heroku
django_heroku.settings(locals())