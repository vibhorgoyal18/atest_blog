from urllib import request
from rest_framework import viewsets, status
from django.contrib.auth.models import User
from atest.serializers import UserSerializer
from rest_framework import permissions
from atest.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset provides operations on Users table to the same user.
    """

    # permission_classes = [IsOwnerOrReadOnly,]
    queryset = User.objects.all()
    serializer_class = UserSerializer
