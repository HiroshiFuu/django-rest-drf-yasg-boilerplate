from django import forms
from django.core import exceptions, validators
from django.utils.translation import gettext, gettext_lazy as _, pgettext
from django.http import HttpResponseRedirect
from django.contrib import messages

from allauth.account import signals
from allauth.account.adapter import get_adapter
from allauth.account.utils import get_login_redirect_url
from allauth.utils import set_form_field_order
from allauth.exceptions import ImmediateHttpResponse


class LoginForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField()

    user = None
    error_messages = {
        "account_inactive": _("This account is currently inactive."),
        "email_password_mismatch": _(
            "The e-mail address and/or password you specified are not correct."
        ),
        "username_password_mismatch": _(
            "The username and/or password you specified are not correct."
        ),
    }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super(LoginForm, self).__init__(*args, **kwargs)
        set_form_field_order(self, ["username", "password"])

    def user_credentials(self):
        credentials = {}
        credentials["username"] = self.cleaned_data["username"]
        credentials["password"] = self.cleaned_data["password"]
        return credentials

    def clean_username(self):
        username = self.cleaned_data["username"]
        return username.strip()

    def clean(self):
        super(LoginForm, self).clean()
        self.cleaned_data["username"] = self.clean_username()
        if self._errors:
            return
        credentials = self.user_credentials()
        user = get_adapter(self.request).authenticate(self.request, **credentials)
        if user:
            self.user = user
        else:
            raise forms.ValidationError(
                self.error_messages["username_password_mismatch"]
            )
        return self.cleaned_data

    def login(self, request, redirect_url=None):
        adapter = get_adapter(request)
        user = self.user
        if not user.is_active:
            return adapter.respond_user_inactive(request, user)
        try:
            adapter.login(request, user)
            response = HttpResponseRedirect(
                get_login_redirect_url(request, redirect_url)
            )

            signal_kwargs = {}
            signals.user_logged_in.send(
                sender=user.__class__,
                request=request,
                response=response,
                user=user,
                **signal_kwargs,
            )
            adapter.add_message(
                request,
                messages.SUCCESS,
                "account/messages/logged_in.txt",
                {"user": user},
            )
        except ImmediateHttpResponse as e:
            response = e.response
        return response
