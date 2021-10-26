"""
Importing default functionality from
contrib.auth packages
"""
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    """
    Form which create user with below
    mention fields as a consideration
    """
    class Meta:
        """
        including the below mentioned fields
        """
        fields = ("username", "email", "password1", "password2")
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Display name"
        self.fields["email"].label = "Email address"
