import os
from settings.local_settings import *

DEBUG = os.environ["DEBUG"]
ALLOWED_HOSTS = list(os.environ["ALLOWED_HOSTS"])
SECRET_KEY = os.environ["SECRET_KEY"]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ.get("NAME"),
        "USER": os.environ.get("USER"),
        "PASSWORD": os.environ.get("PASSWORD"),
        "HOST": os.environ.get("HOST"),
        "PORT": 5432,
    }
}
