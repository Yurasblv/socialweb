import os
from settings.local_settings import *

DEBUG = os.environ["DEBUG"]
ALLOWED_HOSTS = list(os.environ["ALLOWED_HOSTS"])
SECRET_KEY = os.environ["SECRET_KEY"]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": "db",
        "NAME": "greetdb",
        "USER": "greetroot",
        "PASSWORD": "greetpass",
        "PORT": 5432,
    }
}
