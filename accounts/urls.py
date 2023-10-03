from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.shortcuts import render
from . import views
from .views import (UserLoginView, AccountHomePageView, UserSignUpView)
from django.contrib.auth import views as auth_views

app_name= 'accounts'
urlpatterns = [
    path('', AccountHomePageView.as_view(), name='home'),
    path('user-login', auth_views.LoginView.as_view(template_name = 'user-login.html'), name='login'),
    path('profile/', AccountHomePageView.as_view(), name='profile'),
    path('logout', auth_views.LogoutView.as_view(template_name= 'logout.html'), name= 'logout'),
    path('signup', UserSignUpView.as_view(), name='signup'),
    path('password-change', auth_views.PasswordChangeView.as_view(template_name = 'password_change.html')),
    re_path('password_reset', auth_views.PasswordResetView.as_view(template_name = 'registration/forgot_password.html'), name='reset_password'),
    re_path(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view(template_name = 'registration/password_reset_done.html'), name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        auth_views.PasswordResetConfirmView.as_view(template_name = 'registration/password_reset_confirm.html'), name='password_reset_confirm'),
    re_path(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(template_name = 'registration/password_reset_complete.html'), name='password_reset_complete'),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)