from django.urls import re_path

from .base_views import CustomObtainAuthTokenView
from .base_views import ListUserView
from .base_views import QueryUserView
from .base_views import ListRoleView


base_urlpatterns = [
    re_path(r'auth/login$', CustomObtainAuthTokenView.as_view(), name='auth_login'),
    re_path(r'users$', ListUserView.as_view(), name='users'),
    re_path(r'users/token$', QueryUserView.as_view(), name='users-token'),
    re_path(r'roles$', ListRoleView.as_view(), name='role'),
]