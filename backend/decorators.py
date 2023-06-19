from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .constants import ALLOWED_VERSIONS, RESPONSE_401_DATA, RESPONSE_403_DATA, RESPONSE_403_AUTH, RESPONSE_404_VERSION, RESPONSE_500_DATA

import copy


def check_allowed_versions(version=None):
    def decorator_wrapper(view_func):
        def func_wrapper(view_obj, request, *args, **kwargs):
            # print('{0} {1} {2}: {3}'.format(view_obj, request, kwargs, version))
            if request.version not in ALLOWED_VERSIONS:
                return Response(data=RESPONSE_404_VERSION, status=status.HTTP_404_NOT_FOUND)
            if version:
                if request.version != version:
                    return Response(data=RESPONSE_404_VERSION, status=status.HTTP_404_NOT_FOUND)
            return view_func(view_obj, request, *args, **kwargs)
        return func_wrapper
    return decorator_wrapper


def check_token_auth(placeholder=None):
    def decorator_wrapper(view_func):
        def func_wrapper(view_obj, request, *args, **kwargs):
            # print('{0} {1} {2}'.format(view_obj, request, kwargs))
            try:
                token_key = request.auth
                if token_key is None:
                    return Response(data=RESPONSE_403_AUTH, status=status.HTTP_403_FORBIDDEN)
                token = Token.objects.filter(key=token_key).first()
                if not token:
                    res_data = copy.deepcopy(RESPONSE_401_DATA)
                    res_data['message'] = 'Unauthorized with provided token.'
                    return Response(data=res_data, status=status.HTTP_401_UNAUTHORIZED)
            except Exception as e:
                import traceback
                traceback.print_exc()
                res_data = copy.deepcopy(RESPONSE_500_DATA)
                res_data['message'] = traceback.format_exc()
                return Response(data=res_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return view_func(view_obj, request, *args, **kwargs)
        return func_wrapper
    return decorator_wrapper


def restrict_admin(placeholder=None):
    def decorator_wrapper(view_func):
        def func_wrapper(view_obj, request, *args, **kwargs):
            # print('{0} {1} {2}'.format(view_obj, request, kwargs))
            try:
                token_key = request.auth
                if token_key is None:
                    return Response(data=RESPONSE_403_AUTH, status=status.HTTP_403_FORBIDDEN)
                token = Token.objects.filter(key=token_key).first()
                if not token:
                    res_data = copy.deepcopy(RESPONSE_401_DATA)
                    res_data['message'] = 'Unauthorized with provided token.'
                    return Response(data=res_data, status=status.HTTP_401_UNAUTHORIZED)
                user = get_user_model().objects.filter(id=token.user_id).first()
                if user.is_superuser:
                    return Response(data=RESPONSE_403_DATA, status=status.HTTP_403_FORBIDDEN)
            except Exception as e:
                import traceback
                traceback.print_exc()
                res_data = copy.deepcopy(RESPONSE_500_DATA)
                res_data['message'] = traceback.format_exc()
                return Response(data=res_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return view_func(view_obj, request, *args, **kwargs)
        return func_wrapper
    return decorator_wrapper


def conditional_decorator(decorator, condition, *args):

    def wrapper(function):
        if condition(*args):
            return decorator(function)
        else:
            return function

    return wrapper
