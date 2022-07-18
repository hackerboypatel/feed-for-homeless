from dataclasses import fields
from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email', 'password1','password2']
        labels = {'email': 'Enter Valid Email'}
        labels = {'username': 'Enter user name'}
        labels = {'first_name': 'Enter First Name'}
        labels = {'last_name': 'Enter Last Name'}



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
