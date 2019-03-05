from rest_framework import serializers
from comments.models import Comments
from django.contrib.auth.models import User


class CommentsSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comments
        fields = ('url', 'id', 'owner', 'comment', 'blog', 'date_added')
