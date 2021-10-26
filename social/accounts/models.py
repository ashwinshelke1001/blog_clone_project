"""
Importing default packages
"""
from django.contrib import auth

class User(auth.models.User, auth.models.PermissionsMixin):
    """
    creating class using default models
    to use built in functionality
    """

    def __str__(self):
        return "@{}".format(self.username)
    