from rest_framework import serializers
from comments.models import Comments
from users.serializers import CommentUserSerializer


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"
        read_only_fields = ('owner',)


class CommentsViewSerializer(serializers.ModelSerializer):
    owner = CommentUserSerializer()

    class Meta:
        model = Comments
        fields = '__all__'
        depth = 1
