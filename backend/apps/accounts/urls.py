from django.contrib import admin
from django.contrib.auth.views import PasswordChangeDoneView, PasswordChangeView
from django.urls import path, include

from backend.apps.accounts.views import (
    LoginView,
    UserRegisterView,
    RegisterDoneView,
    user_logout,
    UserUpdateView,
)

urlpatterns = [
    path('login/', LoginView.as_view(), name='sign_in'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('register/done/', RegisterDoneView.as_view(), name='register_done'),
    path('logout/', user_logout, name='logout'),
    path('user/profile/update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),

]