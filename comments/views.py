from comments.models import Comments
from comments.serializers import CommentsSerializer
from comments.permissions import IsOwnerOrReadOnly
from rest_framework import viewsets


class CommentViewSet(viewsets.ModelViewSet):
    """
    This viewset provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for user comments.
    """
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def get_queryset(self):
        queryset = self.queryset
        if self.request.query_params.get('blog', False) is False:
            query_set = queryset.filter(blog=self.request.query_params['blog'])
        else:
            query_set = queryset
        return query_set

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
