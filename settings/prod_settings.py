from settings.local_settings import *
import dj_database_url
import django_heroku

DEBUG=False



DATABASES = { 'default':
                  dj_database_url.config(conn_max_age=600)
              }


django_heroku.settings(locals())
