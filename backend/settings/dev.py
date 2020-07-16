"""Use this for development"""

from .base import *

ALLOWED_HOSTS += ['127.0.0.1']
DEBUG = True

WSGI_APPLICATION = 'backend.wsgi.dev.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, Config.get('sqlite_name')),
    }
}

CORS_ORIGIN_WHITELIST = (
    'http://localhost:3000',
)
