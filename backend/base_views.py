from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .decorators import check_allowed_versions, check_token_auth, restrict_admin, conditional_decorator

from .constants import RESPONSE_400_DATA
from .constants import RESPONSE_401_DATA
from .constants import RESPONSE_404_DATA
from .constants import RESPONSE_404_VERSION
from .constants import RESPONSE_404_ENDPOINT
from .constants import RESPONSE_500_DATA
from .constants import ALLOWED_VERSIONS

from .serializers import AuthUserSerializer
from .serializers import AuthTokenExampleSerializer
from .serializers import RoleSerializer
from .serializers import UserSerializer

from core.models import Role

import copy
import os


@conditional_decorator(csrf_exempt, lambda settings: settings['DJANGO_SETTINGS_MODULE'] == 'configuration.settings.develop', os.environ)
def demo(request):
    if request.user.is_authenticated:
        verions = settings.REST_FRAMEWORK['ALLOWED_VERSIONS']
        return render(request, 'home.html', {'verions': verions})
    else:
        return HttpResponseRedirect(reverse('account_login'))


class CustomObtainAuthTokenView(APIView):

    @swagger_auto_schema(operation_description='User log in with username and password', request_body=AuthTokenExampleSerializer, security=[], responses={200: openapi.Response('', AuthUserSerializer)}, tags=['Authentication'])
    @check_allowed_versions(version=None)
    def post(self, request):
        try:
            serializer = AuthTokenExampleSerializer(data=request.data)
            if not serializer.is_valid():
                res_data = copy.deepcopy(RESPONSE_401_DATA)
                res_data['message'] = 'Unable to log in with provided credentials.'
                return Response(data=res_data, status=status.HTTP_401_UNAUTHORIZED)
            user = serializer.validated_data['user']
            token, _ = Token.objects.get_or_create(user=user)
            data = {'username': user.username, 'token': token.key}
            serializer = AuthUserSerializer(data=data)
            if serializer.is_valid():
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(data=copy.deepcopy(RESPONSE_400_DATA), status=status.HTTP_400_BAD_REQUEST)
        except:
            import traceback
            traceback.print_exc()
            res_data = copy.deepcopy(RESPONSE_500_DATA)
            res_data['message'] = traceback.format_exc()
            return Response(data=res_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ListRoleView(APIView):

    @authentication_classes([TokenAuthentication])
    @swagger_auto_schema(operation_description='List roles', responses={200: openapi.Response('', RoleSerializer(many=True))}, tags=['User'])
    @check_allowed_versions(version=None)
    @check_token_auth()
    def get(self, request):
        queryset = Role.objects.all()
        serializer = RoleSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class ListUserView(APIView):

    @authentication_classes([TokenAuthentication])
    @swagger_auto_schema(operation_description='List users', responses={200: openapi.Response('', UserSerializer(many=True))}, tags=['User'])
    @check_allowed_versions(version=None)
    @check_token_auth()
    def get(self, request):
        queryset = User.objects.filter(is_superuser=False)
        serializer = UserSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class QueryUserView(APIView):

    @authentication_classes([TokenAuthentication])
    @swagger_auto_schema(operation_description='Query user profile', responses={200: openapi.Response('', UserSerializer)}, tags=['User'])
    @check_allowed_versions(version=None)
    @check_token_auth()
    def get(self, request):
        token = Token.objects.get(key=request.auth)
        queryset = User.objects.get(id=token.user_id)
        serializer = UserSerializer(queryset)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
