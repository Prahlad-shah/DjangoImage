from django.forms.models import BaseModelForm
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
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
    loginActive = 'active'
    extra_context={'pageTitle': pageTitle, 'pageStatus': pageStatus, 'loginkActive': loginActive }

from django.utils.translation import gettext_lazy as _
from braces.views import FormInvalidMessageMixin
class UserSignUpView(SuccessMessageMixin, CreateView):
    form_class = UserSignUpForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'user_register.html'
    
    pageStatus = 1
    pageTitle = 'Sign Up'
    userSignUPActive = 'active'
    success_message = "Account was created successfully"
    extra_context={'pageTitle': pageTitle, 'pageStatus': pageStatus, 'homekActive': userSignUPActive,
                   'success_message': success_message,}
    
    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Please submit the form Correctly")
        messages.add_message(self.request, messages.ERROR, 'strong password is reccommended.')
        return HttpResponseRedirect('signup')   
    
