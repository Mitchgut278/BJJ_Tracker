from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import *

from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TechniqueForm(ModelForm):
    class Meta:
        model = Technique
        fields = '__all__'
        exclude = ['id']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']