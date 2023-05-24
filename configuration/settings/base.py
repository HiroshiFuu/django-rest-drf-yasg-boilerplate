"""
Base settings

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import environ
import os


# ENVIRONMENT
# ------------------------------------------------------------------------------
# Project/configuration/settings/base.py - 3 = Project/
BASE_DIR = environ.Path(__file__) - 3
PARENT_DIR = BASE_DIR - 1
CORE_DIR = BASE_DIR.path('core')

environ.Env.read_env(BASE_DIR('.env'))  # reading .env file
env = environ.Env()

SENTRY_DSN = os.environ.get('SENTRY_DSN', False)
SENTRY_RELEASE = os.environ.get('SENTRY_RELEASE', False)

VERSION = os.environ.get('VERSION', '0.0.0')
SWAGGER_VALIDATOR_URL = os.environ.get('SWAGGER_VALIDATOR_URL', None)
IPINFO_TOKEN = os.environ.get('IPINFO_TOKEN', None)


# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/4.1/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = 'j8(@n0e203&h0d(v=mix+9o#m#q^4p^s2ro70+88^gynbq%1mv'


# SITE CONFIGURATION
# ------------------------------------------------------------------------------
SITE_ID = 1

FILE_UPLOAD_PERMISSIONS = 0o644

RUNSERVERPLUS_SERVER_ADDRESS_PORT = '0.0.0.0:8080'


# APP CONFIGURATION
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    # Default Django apps:
    'djangocms_admin_style',  # out-of-the-box admin style
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',  # for humanize numbers and dates
    'django.contrib.sites',
]

THIRD_PARTY_APPS = [
    'crispy_forms',  # Form layouts
    'allauth',  # registration
    'allauth.account',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_swagger',
    'drf_yasg',
    'django_extensions',
    'inline_actions',
    'tinymce',
    'import_export',
    'corsheaders',
]

# Apps specific for this project go here.
LOCAL_APPS = [
    # Your stuff: custom apps go here
    'core.apps.CoreConfig',
    'backend.apps.BackendConfig',
]

# See: https://docs.djangoproject.com/en/4.1/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


# CACHING
# ------------------------------------------------------------------------------
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}


# DEBUG
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/4.1/ref/settings/#debug
DEBUG = False


# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/4.1/ref/settings/#databases
# Uses django-environ to accept uri format
# See: https://django-environ.readthedocs.io/en/latest/#supported-types
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'HOST': env('DATABASE_HOST'),
        'PORT': env('DATABASE_PORT'),
    }
}

DATABASES['default']['ATOMIC_REQUESTS'] = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'


# EMAIL CONFIGURATION
# ------------------------------------------------------------------------------
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587
EMAIL_USE_TLS = True


# MIDDLEWARE CONFIGURATION
# ------------------------------------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'core.middleware.CurrentUserMiddleware',
]


# MIGRATIONS CONFIGURATION
# ------------------------------------------------------------------------------
MIGRATION_MODULES = {
    'sites': 'django.contrib.sites.migrations'
}


# URL CONFIGURATION
# ------------------------------------------------------------------------------
ROOT_URLCONF = 'configuration.urls'

# Location of root django.contrib.admin URL, use {% url 'admin:index' %}
ADMIN_URL = r'^admin/'

# See: https://docs.djangoproject.com/en/4.1/ref/settings/#wsgi-application
WSGI_APPLICATION = 'configuration.wsgi.application'


# STATIC FILE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/4.1/ref/settings/#static-root
STATIC_ROOT = str(PARENT_DIR('STATIC_ROOT'))

# See: https://docs.djangoproject.com/en/4.1/ref/settings/#static-url
STATIC_URL = '/static/'

# See: https://docs.djangoproject.com/en/4.1/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [
    str(BASE_DIR.path('core', 'static')),
    str(BASE_DIR.path('backend', 'static')),
]

# See: https://docs.djangoproject.com/en/4.1/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]


# MEDIA CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/4.1/ref/settings/#media-root
MEDIA_ROOT = str(CORE_DIR('media'))

# See: https://docs.djangoproject.com/en/4.1/ref/settings/#media-url
MEDIA_URL = '/media/'


# MANAGER CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/4.1/ref/settings/#admins
ADMINS = [
    ("FENG Hao", 'hiroshifuu@outlook.com'),
]

# See: https://docs.djangoproject.com/en/4.1/ref/settings/#managers
MANAGERS = ADMINS


# TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/4.1/ref/settings/#templates
TEMPLATES = [
    {
        # See: https://docs.djangoproject.com/en/4.1/ref/settings/#std:setting-TEMPLATES-BACKEND
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # See: https://docs.djangoproject.com/en/4.1/ref/settings/#template-dirs
        'DIRS': [
            str(CORE_DIR.path('templates')),
            # str(BASE_DIR.path('apps').path('admin_portal').path('templates')),
        ],
        'OPTIONS': {
            # See: https://docs.djangoproject.com/en/4.1/ref/settings/#template-debug
            'debug': DEBUG,
            # See: https://docs.djangoproject.com/en/4.1/ref/settings/#template-loaders
            # https://docs.djangoproject.com/en/4.1/ref/templates/api/#loader-types
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            # See: https://docs.djangoproject.com/en/4.1/ref/settings/#template-context-processors
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                # Your stuff: custom template context processors go here
            ],
        },
    },
]

# See: http://django-crispy-forms.readthedocs.io/en/latest/install.html#template-packs
CRISPY_TEMPLATE_PACK = 'bootstrap4'


# LOGGING
# ------------------------------------------------------------------------------
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'INFO',
        },
        'werkzeug': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'WARNING',
            'propagate': False,
        },
    },
}


# LANGUAGE CONFIGURATION
# ------------------------------------------------------------------------------
# If you set to False, Django will make some optimizations so as not
# to load the internationalization machinery.

# See: https://docs.djangoproject.com/en/4.1/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/4.1/ref/settings/#use-l10n
USE_L10N = True

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
# See: https://docs.djangoproject.com/en/4.1/ref/settings/#language-code
LANGUAGE_CODE = 'en-us'

# Languages we provide translations for, out of the box.
LANGUAGES = [
    ('en-us', 'English'),
    ('zh-hans', 'Simplified Chinese'),
    ('zh-hant', 'Traditional Chinese'),
]


# TIMEZONE CONFIGURATION
# ------------------------------------------------------------------------------
# Time zone support is disabled and uses pytz disabled by default.
# See: https://docs.djangoproject.com/en/4.1/ref/settings/#use-tz
USE_TZ = True

# Local time zone for this installation. Choices can be found here:
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Asia/Singapore'


# PASSWORD STORAGE SETTINGS
# ------------------------------------------------------------------------------
# See https://docs.djangoproject.com/en/4.1/topics/auth/passwords/#using-argon2-with-django
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.ScryptPasswordHasher',
]


# PASSWORD VALIDATION
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators
# ------------------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
    {
        'NAME': 'core.password_validation.UpperLowerNumericPasswordValidator',
    }
]


# AUTHENTICATION CONFIGURATION
# ------------------------------------------------------------------------------
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

# FOR ACCOUNT SETTING
ACCOUNT_AUTHENTICATION_METHOD = 'username'
# ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_USERNAME_REQUIRED = True
# ACCOUNT_EMAIL_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = 'none'
# ACCOUNT_USER_MODEL_USERNAME_FIELD = 'email'
ACCOUNT_ALLOW_REGISTRATION = True
ACCOUNT_UNIQUE_EMAIL = False  # do not asking for unique email address
LOGIN_URL = 'account_login'
LOGIN_REDIRECT_URL = '/'
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5

# SLUGLIFIER
AUTOSLUG_SLUGIFY_FUNCTION = 'slugify.slugify'


# REST FRAMEWORK
# ------------------------------------------------------------------------------
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'core.authentication_class.BearerAuthentication',
        'core.authentication_class.TokenAuthentication'
    ],
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning',
    # 'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning',
    'ALLOWED_VERSIONS': ['v1', 'v2'],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ],
    'COERCE_DECIMAL_TO_STRING': False,
}


# SWAGGER
# ------------------------------------------------------------------------------
from django_validated_jsonfield.yasg import DEFAULT_FIELD_INSPECTORS    # isort:skip    # noqa: C0415
SWAGGER_SETTINGS = {
    # 'DEFAULT_AUTO_SCHEMA_CLASS': 'core.yasg_auto_schema.NameAsOperationIDAutoSchema',
    'DEFAULT_AUTO_SCHEMA_CLASS': 'core.yasg_auto_schema.SwaggerExampleAutoSchema',
    'JSON_EDITOR': True,
    'DOC_EXPANSION': 'none',
    'SECURITY_DEFINITIONS': {
        'api_key': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header',
        },
    },
    'USE_SESSION_AUTH': False,
    'IS_AUTHENTICATED': False,
    'DISPLAY_OPERATION_ID': False,
    'DEFAULT_FIELD_INSPECTORS': DEFAULT_FIELD_INSPECTORS
}


# DJANGO JSON WIDGET CONFIGURATION
JSON_EDITOR_JS = 'jsoneditor/jsoneditor.js'
JSON_EDITOR_CSS = 'jsoneditor/jsoneditor.css'


# DJANGO TINYMCE CONFIGURATION
TINYMCE_DEFAULT_CONFIG = {
    'plugins': 'print preview paste searchreplace autolink autosave save directionality code visualblocks visualchars fullscreen image link media template charmap hr advlist lists wordcount imagetools textpattern help charmap emoticons',
    'cleanup_on_startup': True,
}


# django-corsheaders
# ------------------------------------------------------------------------------
MIDDLEWARE.insert(2, 'corsheaders.middleware.CorsMiddleware')

CORS_ALLOW_CREDENTIALS = True

from corsheaders.defaults import default_headers    # noqa  # isort: skip
CORS_ALLOW_HEADERS = list(default_headers) + [
    'content-disposition',
    'origin',
    'x-csrftoken',
]

CORS_EXPOSE_HEADERS = ['content-disposition']
