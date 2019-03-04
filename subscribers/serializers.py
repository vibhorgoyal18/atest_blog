from rest_framework import serializers
from django.contrib.auth.models import User
from subscribers.models import Subscribers


class SubscribersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subscribers
        fields = '__all__'
