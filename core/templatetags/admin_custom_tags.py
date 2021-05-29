from django import template
from django.contrib.sites.shortcuts import get_current_site
from django.template.defaultfilters import conditional_escape
from django.template.loader import render_to_string


register = template.Library()


@register.simple_tag(takes_context=True)
def current_site_domain(context):
    request = context.get('request')

    try:
        site_domain = get_current_site(request).domain
    except AttributeError:
        # This happens if request is None
        # and sites framework is not in INSTALLED_APPS
        site_domain = request.get_host()
    return conditional_escape(site_domain)
