from django.forms.models import BaseModelForm
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import FormMixin
from django.views.generic import ListView, TemplateView, CreateView
from .ac_form import UserSignUpForm, UserCreationForm, CustomUserChangeForm


relative_path_profile = 'https://mdbcdn.b-cdn.net/img/new/avatars/1.webp'

# Create your views here.
class AccountHomePageView(TemplateView):
    template_name = 'home.html'
    pageTitle = "Homepage"
    pageStatus = '1'
    homeActive = 'active'
    extra_context={'pageTitle': pageTitle, 'pageStatus': pageStatus, 'homekActive': homeActive,
                   'relative_path_profile': relative_path_profile,}

    


class UserLoginView(TemplateView, FormMixin):
    template_name = 'user-login.html'
    pageStatus = 1
    pageTitle = 'Login'
    loginActive = 'active'
    extra_context={'pageTitle': pageTitle, 'pageStatus': pageStatus, 'loginkActive': loginActive,
                   }
    

from django.utils.translation import gettext_lazy as _
from braces.views import FormInvalidMessageMixin
class UserSignUpView(SuccessMessageMixin, CreateView):
    form_class = UserSignUpForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'user_register.html'
    
    pageStatus = 1
    pageTitle = 'Sign Up'
    userSignUPActive = 'active'
    extra_context={'pageTitle': pageTitle, 'pageStatus': pageStatus, 'homekActive': userSignUPActive,
                   }
    
    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Please submit the form Correctly")
        messages.add_message(self.request, messages.ERROR, 'strong password is reccommended.')
        return HttpResponseRedirect('signup')   
    
from io import BytesIO
from django.conf import settings
from pathlib import Path
from datetime import datetime
from io import BytesIO
from django.conf import settings
from subscriptable_path import Path as s_path
import glob
import os
import pickle
from PIL import Image   
def profilePicture(request):
    profileActive = 'active'
    pageTitle = 'Image Search'
    pageStatus = 1
    relative_path_profile = 'https://mdbcdn.b-cdn.net/img/new/avatars/1.webp'
    upload_dir = Path(str(settings.MEDIA_ROOT)+'/user_profiles/')
    root_dir = Path(str(settings.MEDIA_ROOT)+'/Flickr_32')
    if request.method == 'POST' and request.FILES['imagefile']:
        image = request.FILES['imagefile']
        pageStatus = 2
        # Save query image
        buffer = BytesIO()
        buffer.write(image.read())
        buffer.seek(0)
        img = Image.open(buffer)  # PIL image
        uploaded_img_path_url = Path(str(upload_dir) + '/' +datetime.now().isoformat().replace(":", ".") + "_" + image.name)
        img.save(uploaded_img_path_url)
        path = uploaded_img_path_url #FULL PATH
        start = settings.MEDIA_ROOT
        relative_path = os.path.relpath(path, start)
        relative_path_profile = '/' + relative_path
        request.user.profileIMG = relative_path_profile
        request.user.save()
        return render(request, 'home.html', {
		'pageStatus':pageStatus,
		'pageTitle':pageTitle,
		'profileActive':profileActive,
		'settingsBASE_DIR': settings.BASE_DIR,
		'upload_dir': upload_dir,
        'relative_path_profile': relative_path_profile,
		'settingsMEDI_DIR': settings.MEDIA_ROOT,
		
		})
        
    return render(request, 'userprofile/user_profile.html', {
		'pageStatus':pageStatus,
		'pageTitle':pageTitle,
		'profileActive':profileActive,
		'settingsBASE_DIR': settings.BASE_DIR,
		'upload_dir': upload_dir,
        'relative_path_profile': relative_path_profile,
		'settingsMEDI_DIR': settings.MEDIA_ROOT,
		})