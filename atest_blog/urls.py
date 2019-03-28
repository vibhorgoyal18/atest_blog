from django.conf.urls import include, url
from django.urls import path
from rest_framework.routers import DefaultRouter
from contact.views import  SendMail
from users.views import UserViewSet
from comments.views import CommentViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'api/users', UserViewSet)
router.register(r'api/comments', CommentViewSet)
router.register(r'api/contact', SendMail, basename='sendMail')

urlpatterns = [
    url(r'^', include(router.urls)),
    path('api/login/', obtain_auth_token, name='api-token-auth')
]
