from django.urls import path
from .views import RegisterAPIView, UserListAPIView, ChangePasswordView

urlpatterns = [
    path('list', UserListAPIView.as_view(), name='users-list'),
    path('register', RegisterAPIView.as_view(), name='register'),
    path('password-change', ChangePasswordView.as_view(), name='password-change')
]