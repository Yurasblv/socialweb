from settings.local_settings import *
import dj_database_url
import django_heroku
import os

DEBUG = False
ALLOWED_HOSTS = ["*"]


DATABASES = {"default": dj_database_url.config(conn_max_age=600)}
SECRET_KEY = os.environ['SECRET_KEY']


django_heroku.settings(locals())
