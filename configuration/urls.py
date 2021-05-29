from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.urls import re_path
from django.contrib import admin
from django.contrib.sites.models import Site
from django.views import defaults as default_views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

# from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from core.views import index

from onetimelink import presettings

# admin.site.unregister(Site)
admin.site.site_header = 'MyTemplate Administration'
admin.site.index_title = 'MyTemplate'
admin.site.site_title = 'Admin'

schema_view = get_schema_view(
    openapi.Info(
        title='MyTemplate API',
        default_version='v1',
        description='For MyTemplate',
        contact=openapi.Contact(email='hiroshifuu@outlook.com'),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    url(r'^favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico'))),

    # Django Admin, use {% url 'admin:index' %}
    url(settings.ADMIN_URL, admin.site.urls),

    url(r'^accounts/', include('allauth.urls')),

    url(r'^$', index, name='home'),

    url(r'^%s/' % presettings.DYNAMIC_LINK_URL_BASE_COMPONENT, include('onetimelink.urls')),

    url(r'^v1/', ([url(r'swagger-ui/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')], None, 'v1')),
    re_path('api/v1/', include('backend.v1.urls', namespace='v1')),
    url(r'^v2/', ([url(r'swagger-ui/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')], None, 'v2')),
    re_path('api/v2/', include('backend.v2.urls', namespace='v2')),
]

urlpatterns += static('static', document_root=settings.STATIC_ROOT)
urlpatterns += static('media', document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns
