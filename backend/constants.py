from django.conf import settings
from django.utils.translation import gettext as _


REST_FRAMEWORK = getattr(settings, 'REST_FRAMEWORK', None)
ALLOWED_VERSIONS = REST_FRAMEWORK.get('ALLOWED_VERSIONS', '')

RESPONSE_400_DATA = {
    'status': 400,
    'error': 'BAD REQUEST',
    'message': None
}

RESPONSE_401_DATA = {
    'status': 401,
    'error': 'UNAUTHORIZED',
    'message': None
}

RESPONSE_403_DATA = {
    'status': 403,
    'error': 'FORBIDDEN',
    'message': 'Superuser is not allowed'
}

RESPONSE_403_AUTH = {
    'status': 403,
    'error': 'FORBIDDEN',
    'message': 'authroization token is required'
}

RESPONSE_404_DATA = {
    'status': 404,
    'error': 'NOT FOUND',
    'message': None
}

RESPONSE_404_VERSION = {
    'status': 404,
    'error': 'NOT FOUND',
    'message': 'version number not found'
}

RESPONSE_404_ENDPOINT = {
    'status': 404,
    'error': 'NOT FOUND',
    'message': 'this endpoint does not exist'
}

RESPONSE_500_DATA = {
    'status': 500,
    'error': 'INTERNAL SERVER ERROR',
    'message': None
}
