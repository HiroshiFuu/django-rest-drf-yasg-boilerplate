from django.urls import re_path

from .views import *

app_name = 'backend'

urlpatterns = [
    re_path(r'list_shape_by_type/(?P<shape_type>[a-z]{1,15})$', ListShapeByTypeView.as_view(), name='list_shape_by_type'),
    re_path(r'crud_shape$', PostUpdateShapeView.as_view(), name='post_update_shape'),
    re_path(r'crud_shape/(?P<shape_id>[0-9]{1,7})$', ReadDeleteShapeView.as_view(), name='read_delete_shape'),
]

from ..base_urls import base_urlpatterns
urlpatterns += base_urlpatterns
