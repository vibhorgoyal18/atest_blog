from django.urls import path
from users.views import CreateUserView, PassResetView, UserSelfRetrieveView, UserSelfUpdateView, ChangePasswordView

app_name = 'users'

urlpatterns = [
    path('new-user', CreateUserView.as_view(), name='new-user'),
    path('me', UserSelfRetrieveView.as_view(), name='me'),
    path('me-edit', UserSelfUpdateView.as_view(), name='me-edit'),
    path('reset-pass', PassResetView.as_view(), name='reset-pass'),
    path('change-pass', ChangePasswordView.as_view(), name='change-pass'),
]
