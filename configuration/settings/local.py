"""
Local settings
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


# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = '_zbw*zp4w^l7%eidp%t#@y(5&0$f9p4ejmy+@^bsg72e7w5!i!'


# Mail settings
# ------------------------------------------------------------------------------
EMAIL_HOST = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
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

# DATABASES
# ------------------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(str(ROOT_DIR), 'db.sqlite3'),
    }
}