"""
Base settings

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""
import os
import environ


# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = 'j8(@n0e203&h0d(v=mix+9o#m#q^4p^s2ro70+88^gynbq%1mv'


# (Project/configuration/settings/base.py - 3 = Project/)
ROOT_DIR = environ.Path(__file__) - 3
PARENT_DIR = ROOT_DIR - 1
CORE_DIR = ROOT_DIR.path('core')
environ.Env.read_env(ROOT_DIR('.env'))  # reading .env file


# APP CONFIGURATION
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    # Default Django apps:
    'djangocms_admin_style', # out-of-the-box admin style
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
    'allauth.socialaccount',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_swagger',
    'phonenumber_field',
    'drf_yasg',
    'inline_actions',
    'django_extensions',
    'adminsortable2',
    'onetimelink',
]

# Apps specific for this project go here.
LOCAL_APPS = [
    # Your stuff: custom apps go here
    'core',
    'backend',
]

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


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
    'sites': 'core.contrib.sites.migrations'
}


# DEBUG
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = False


# MANAGER CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = [
    ("FENG Hao", 'hiroshifuu@outlook.com'),
]

# Location of root django.contrib.admin URL, use {% url 'admin:index' %}
ADMIN_URL = r'^admin/'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS


# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
# Uses django-environ to accept uri format
# See: https://django-environ.readthedocs.io/en/latest/#supported-types
DATABASES = {
    'default': {
        'ENGINE': '',
    }
}
DATABASES['default']['ATOMIC_REQUESTS'] = True


# TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
        'DIRS': [
            str(CORE_DIR.path('templates')),
            # str(ROOT_DIR.path('apps').path('admin_portal').path('templates')),
        ],
        'OPTIONS': {
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
            'debug': DEBUG,
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
            # https://docs.djangoproject.com/en/dev/ref/templates/api/#loader-types
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
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


# LOGGING CONFIGURATION
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
    },
}


# STATIC FILE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = str(PARENT_DIR('STATIC_ROOT', 'static'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [
    str(ROOT_DIR.path('core', 'static')),
    str(ROOT_DIR.path('backend', 'static')),
]

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]


# MEDIA CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = str(CORE_DIR('media'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'


# URL Configuration
# ------------------------------------------------------------------------------
ROOT_URLCONF = 'configuration.urls'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = 'configuration.wsgi.application'


# PASSWORD STORAGE SETTINGS
# ------------------------------------------------------------------------------
# See https://docs.djangoproject.com/en/dev/topics/auth/passwords/#using-argon2-with-django
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
]


# PASSWORD VALIDATION
# ------------------------------------------------------------------------------
# See https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
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
# LOGIN_REDIRECT_URL = '/'
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 3


# GENERAL CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# SLUGLIFIER
AUTOSLUG_SLUGIFY_FUNCTION = 'slugify.slugify'

# Location of root django.contrib.admin URL, use {% url 'admin:index' %}
ADMIN_URL = r'^admin/'


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


# SWAGGER CONFIGURATION
# ------------------------------------------------------------------------------
from django_validated_jsonfield.yasg import DEFAULT_FIELD_INSPECTORS
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


# EMAIL CONFIGURATION
# ------------------------------------------------------------------------------
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587
EMAIL_USE_TLS = True


# LANGUAGE CONFIGURATION
# ------------------------------------------------------------------------------
# If you set to False, Django will make some optimizations so as not
# to load the internationalization machinery.

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
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
# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True

# Local time zone for this installation. Choices can be found here:
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Etc/GMT0'


# DJANGO JSON WIDGET CONFIGURATION
JSON_EDITOR_JS = 'jsoneditor/jsoneditor.js'
JSON_EDITOR_CSS = 'jsoneditor/jsoneditor.css'
