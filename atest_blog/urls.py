from django.urls import path, include
from contact.views import ContactView
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='My API')

urlpatterns = [
    path('comment/', include('comments.urls', namespace='comments')),
    path('user/', include('users.urls', namespace='user')),
    path('auth/', include('django_expiring_token.urls'), name='api-token-auth'),
    path('contact', ContactView.as_view(), name='contact'),
    path('', schema_view, name='api-root'),
]
