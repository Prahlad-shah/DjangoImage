from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView
from .ac_form import UserSignUpForm, UserCreationForm

# Create your views here.
class AccountHomePageView(TemplateView):
    template_name = 'home.html'
    pageTitle = "Homepage"
    pageStatus = '1'
    homeActive = 'active'
    extra_context={'pageTitle': pageTitle, 'pageStatus': pageStatus, 'homekActive': homeActive }

    


class UserLoginView(TemplateView):
    template_name = 'home.html'
    pageStatus = 1
    pageTitle = 'Login'
    homeActive = 'active'
    extra_context={'pageTitle': pageTitle, 'pageStatus': pageStatus, 'homekActive': homeActive }


class UserSignUpView(CreateView):
    form_class = UserSignUpForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'user_register.html'
    pageStatus = 1
    pageTitle = 'Sign Up'
    
