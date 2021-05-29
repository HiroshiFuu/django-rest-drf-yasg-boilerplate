"""
Develop settings
"""
from .base import *  # noqa
import os


# DEBUG
# ------------------------------------------------------------------------------
DEBUG = True
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG


# SITE CONFIGURATION
# ------------------------------------------------------------------------------
# Hosts/domain names that are valid for this site
# See https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
# ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=['hiroshifuu.xyz', ])
ALLOWED_HOSTS = ['*']

INTERNAL_IPS = ['127.0.0.1']

RUNSERVERPLUS_SERVER_ADDRESS_PORT = '0.0.0.0:8080'


# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = 'vtfup+su5gi^o_0in_ne)#$l9gnyljo&v*xl0y@twf+85k79)f'


# Mail settings
# ------------------------------------------------------------------------------
EMAIL_HOST = os.environ.get('STMP_HOST')
EMAIL_HOST_USER = os.environ.get('STMP_USERNAME')
EMAIL_HOST_PASSWORD = os.environ.get('STMP_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True


# CACHING
# ------------------------------------------------------------------------------
CACHES = {
	'default': {
		'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
		'LOCATION': ''
	}
}


# env-apps
# ------------------------------------------------------------------------------
INSTALLED_APPS += [
    'debug_toolbar',
    'corsheaders',
]


# django-debug-toolbar
# ------------------------------------------------------------------------------
MIDDLEWARE += [
	'debug_toolbar.middleware.DebugToolbarMiddleware',
]

DEBUG_TOOLBAR_CONFIG = {
	'DISABLE_PANELS': [
		'debug_toolbar.panels.redirects.RedirectsPanel',
	],
	'SHOW_TEMPLATE_CONTEXT': True,
}


# django-corsheaders
# ------------------------------------------------------------------------------
MIDDLEWARE += [
    'corsheaders.middleware.CorsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True

from corsheaders.defaults import default_headers
CORS_ALLOW_HEADERS = list(default_headers) + [
    'content-disposition'
]


# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
# Uses django-environ to accept uri format
# See: https://django-environ.readthedocs.io/en/latest/#supported-types
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DATABASE_NAME'),
        'USER': os.environ.get('DATABASE_USER'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'HOST': os.environ.get('DATABASE_HOST'),
        'PORT': os.environ.get('DATABASE_POST'),
    }
}

DATABASES['default']['ATOMIC_REQUESTS'] = True
