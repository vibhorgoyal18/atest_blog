from django.conf.urls import include, url
from django.urls import path
from rest_framework.routers import DefaultRouter
from contact.views import  SendMail
from users.views import UserViewSet
from comments.views import CommentViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'sendmail', SendMail, basename='sendMail')

urlpatterns = [
    url(r'^', include(router.urls)),
    path('login/', obtain_auth_token, name='api-token-auth')
]
