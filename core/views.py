# -*- coding:utf-8 -*-
from django import http
from django.urls import reverse
from django.shortcuts import render
from django.conf import settings

import logging
logger = logging.getLogger(__name__)


def index(request):
    if request.user.is_authenticated:
        verions = settings.REST_FRAMEWORK['ALLOWED_VERSIONS']
        return render(request, 'home.html', {'verions': verions})
    else:
        return http.HttpResponseRedirect(reverse('account_login'))
