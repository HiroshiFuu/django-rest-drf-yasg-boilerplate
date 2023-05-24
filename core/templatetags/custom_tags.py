from django import template
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.utils.html import conditional_escape


register = template.Library()


@register.simple_tag(takes_context=True)
def current_site_domain(context):
    request = context.get('request')
    try:
        site_domain = get_current_site(request).domain
    except AttributeError:
        # This happens if request is None and sites framework is not in INSTALLED_APPS
        site_domain = request.get_host()
    return conditional_escape(site_domain)


@register.simple_tag
def settings_value(name):
    val = getattr(settings, name, None)
    if val is None:
        val = ""
    return val
