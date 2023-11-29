from django.forms import ModelForm
from .models import  CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('age',)
    
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields

class UserSignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name', 'email', 'username', 'password1','password2', ]
        
