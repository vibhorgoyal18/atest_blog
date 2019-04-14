from django.urls import path
from comments.views import CommentListView, CommentAddView

app_name = 'comment'

urlpatterns = [
    path('add', CommentAddView.as_view(), name='add-comment'),
    path('list', CommentListView.as_view(), name='list-comments'),
]
