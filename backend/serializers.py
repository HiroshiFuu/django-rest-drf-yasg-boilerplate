from django.conf import settings

from django_validated_jsonfield import ValidatedJsonModelSerializerMixin
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer

from core.models import Profile, Role


class AuthTokenExampleSerializer(AuthTokenSerializer):

    class Meta:
        examples = {
            'username': 'user1',
            'password': '!234Rewq',
        }


class AuthUserSerializer(serializers.Serializer):
    username = serializers.CharField(label='Username')
    token = serializers.CharField(label='Token')

    class Meta:
        fields = ('username', 'token')
        examples = {
            'username': 'user1',
            'token': 'Bearer or Token',
        }


class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = ('name',)


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    role = serializers.CharField(source='profile.role.name')
    timezone = serializers.CharField(source='profile.timezone')

    def get_full_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name)

    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ('id', 'full_name', 'email', 'role', 'timezone')
        examples = {
            'full_name': 'GivenName FamilyName',
            'email': 'E-mail',
            'role': 'Role',
            'timezone': 'Timezone',
        }


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ('first_name', 'last_name', 'email', 'username', 'password')
        extra_kwargs = {
            'username': {'required': True},
            'password': {'required': True},
        }
