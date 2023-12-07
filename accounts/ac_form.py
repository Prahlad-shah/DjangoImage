from django import forms
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, FileInput,BaseModelForm
from .models import  CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('age', 'profileIMG')

    
class CustomUserChangeForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields
        fields = ['email', 'password']

        
class UserSignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name', 'email', 'username', 'profileIMG', 'password1', 'password2']
        widgets = {
            'first_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'First Name'
                }),
            'last_name': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Last Name'
                }),
            'username': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Username'
                }),
            'profileIMG': FileInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;'
                }),
            'email': EmailInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Email'
                }),
            'password': PasswordInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Password'
                }),
            'password2': forms.PasswordInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Confirm Password'
                }),
                    }
