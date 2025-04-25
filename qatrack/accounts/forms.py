from django import forms
from django.contrib.auth.forms import AuthenticationForm as BaseAuthenticationForm
from django.contrib.auth.views import PasswordChangeForm
from django.contrib.auth.views import SetPasswordForm as SetPasswordFormBase
from django_registration.forms import RegistrationForm
from django.utils.translation import gettext_lazy as _


class RegisterForm(RegistrationForm):
    pass


class ChangePasswordForm(PasswordChangeForm):
    pass


class SetPasswordForm(SetPasswordFormBase):
    pass

class CustomAuthenticationForm(BaseAuthenticationForm):
    username = forms.CharField(
        label=_("Nombre de usuario"),  # Set your desired label here
        strip=False, # Keep strip=False as in the original if needed
        widget=forms.TextInput(attrs={'autofocus': True}) # Keep original widget if desired
    )

    password = forms.CharField(
        label=_("Contraseña"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
    )
