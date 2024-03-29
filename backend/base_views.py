from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import authentication_classes
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Role

from .constants import ALLOWED_VERSIONS, RESPONSE_400_DATA, RESPONSE_401_DATA, RESPONSE_403_DATA, RESPONSE_404_DATA, RESPONSE_404_ENDPOINT, RESPONSE_404_VERSION, RESPONSE_500_DATA
from .decorators import check_allowed_versions, check_token_auth, conditional_decorator, restrict_admin
from .serializers import *

import copy
import os
import traceback


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
            traceback.print_exc()
            res_data = copy.deepcopy(RESPONSE_500_DATA)
            res_data['message'] = traceback.format_exc()
            return Response(data=res_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class RegistrationView(APIView):

    @authentication_classes([TokenAuthentication])
    @swagger_auto_schema(operation_description='Create an user', request_body=AccountSerializer, responses={200: openapi.Response('', AccountSerializer)}, tags=['Account'])
    @check_allowed_versions(version=None)
    @check_token_auth()
    def post(self, request):
        user = settings.AUTH_USER_MODEL.objects.get(id=Token.objects.get(key=request.auth).user_id)
        if not user or not user.is_staff:
            res_data = copy.deepcopy(RESPONSE_403_DATA)
            res_data['message'] = 'Only admins are allowed to create users'
            return Response(data=res_data, status=status.HTTP_403_FORBIDDEN)
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            user = settings.AUTH_USER_MODEL.objects.create(
                username=serializer.data.get('username'),
                email=serializer.data.get('email'),
                first_name=serializer.data.get('first_name'),
                last_name=serializer.data.get('last_name')
            )
            user.set_password(serializer.data.get('password'))
            user.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
        queryset = settings.AUTH_USER_MODEL.objects.filter(is_superuser=False)
        serializer = UserSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class QueryUserView(APIView):

    @authentication_classes([TokenAuthentication])
    @swagger_auto_schema(operation_description='Query user profile', responses={200: openapi.Response('', UserSerializer)}, tags=['User'])
    @check_allowed_versions(version=None)
    @check_token_auth()
    def get(self, request):
        token = Token.objects.get(key=request.auth)
        queryset = settings.AUTH_USER_MODEL.objects.get(id=token.user_id)
        serializer = UserSerializer(queryset)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
