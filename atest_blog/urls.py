from django.urls import path, include
from contact.views import ContactView
from comments.views import CommentViewSet
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='My API')

urlpatterns = [

    path('comments', CommentViewSet.as_view({'get': 'list'}), name='comments'),
    path('contact', ContactView.as_view(), name='contact'),
    path('user/', include('users.urls', namespace='user')),
    path('auth/', include('django_expiring_token.urls'), name='api-token-auth'),
    path('', schema_view, name='api-root'),
]
