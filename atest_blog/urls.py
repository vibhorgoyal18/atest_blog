from django.conf.urls import include, url
from django.urls import path
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from atest.views import UserViewSet
from rest_framework.authtoken import views
from comments.views import CommentViewSet

API_TITLE = 'Test API'
API_DESCRIPTION = 'A Web API for creating and viewing highlighted code snippets.'
schema_view = get_schema_view(title=API_TITLE)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^schema/$', schema_view),
    url(r'^docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth')
]
