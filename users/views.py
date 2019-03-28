from rest_framework import viewsets
from users.models import User
from users.serializers import UserSerializer
from users.permissions import UserPermissions
import sendgrid
from sendgrid.helpers.mail import *
import re


class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset provides operations on Users table to the same user.
    """

    permission_classes = [UserPermissions, ]
    queryset = User.objects.all()
    serializer_class = UserSerializer
