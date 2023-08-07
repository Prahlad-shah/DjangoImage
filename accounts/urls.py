from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
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
    path('password-reset', auth_views.PasswordResetView.as_view(template_name = 'forgot_password.html'), name='reset_password'),
    

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)