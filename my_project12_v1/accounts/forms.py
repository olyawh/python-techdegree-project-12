from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import Profile, Skill


class UserCreateForm(UserCreationForm):
    '''User creation form'''
    class Meta:
        fields = (
            'username', 'email', 'password1', 'password2'
        )
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Display name'
        self.fields['email'].label = 'Email address'    


class UserUpdateForm(forms.ModelForm):
    '''User update form'''
    class Meta:
        fields = (
            'username', 'email'
        )
        model = get_user_model()


class ProfileUpdateForm(forms.ModelForm):
    '''Profile update form'''    
    class Meta:
        model = Profile  
        fields = (
            'avatar',
        )  
