from comments.models import Comments
from comments.serializers import CommentsSerializer, CommentsViewSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.request import Request
from comments.models import Comments
from django.http import JsonResponse


class CommentAddView(CreateAPIView):
    """
    This view provides logged in user the access to add comments
    """
    serializer_class = CommentsSerializer
    permission_classes = (IsAuthenticated,)
    model = Comments

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            self.perform_create(serializer)
            return JsonResponse({'success': True}, status=200)

        except Exception as e:
            return JsonResponse({'message': format(e.args[-1]), 'success': False}, status=500)


class CommentListView(ListAPIView):
    """
    This view list of comments
    """
    serializer_class = CommentsViewSerializer
    model = Comments
    queryset = Comments.objects.all().order_by('-date_added')

    def get_queryset(self):
        if 'blog' not in self.request.query_params:
            raise Exception('Blog endpoint URL is required')
        qs = super().get_queryset()
        params = self.request.query_params['blog']
        qs = qs.filter(blog=params)
        return qs

    def list(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(self.get_queryset(), many=True)
            if not serializer.data:
                return JsonResponse({'success': False, 'message': 'Not Found.'}, status=404)
            return JsonResponse({'success': True, 'data': serializer.data}, status=200)
        except Exception as e:
            if e.args[0] == 'Blog endpoint URL is required':
                return JsonResponse({'success': False, 'message': format(e.args[-1])}, status=400)
            return JsonResponse({'success': False, 'message': format(e.args[-1])}, status=500)
