"""Use this for production"""

from .base import *

DEBUG = False
ALLOWED_HOSTS += [Config.get('site_uri')]
WSGI_APPLICATION = 'backend.wsgi.prod.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': Config.get('psql_host'),
        'NAME': Config.get('psql_name'),
        'USER': Config.get('psql_user'),
        'PASSWORD': Config.get('psql_password'),
        'PORT': '',
    }
}
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
