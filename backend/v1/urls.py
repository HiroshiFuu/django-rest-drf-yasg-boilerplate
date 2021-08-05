from django.urls import re_path

app_name = 'backend'

urlpatterns = [
]

from ..base_urls import base_urlpatterns
urlpatterns += base_urlpatterns
