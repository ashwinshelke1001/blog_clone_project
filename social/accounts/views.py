"""view  for accounts"""
from django import forms
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from . import forms

class SignUp(CreateView):
    """
    Display the signup template and handle
    the action for it and after successful compilation
    return to the 'test' url
    """
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("test")
    template_name = "accounts/signup.html"
    