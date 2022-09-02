from dataclasses import fields
from django import forms
from django.forms import ModelForm, DateInput
from .models import *

from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TechniqueForm(ModelForm):
    class Meta:
        model = Technique
        fields = '__all__'
        exclude = ['id', 'user']


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':'form-control', 'placeholder': 'Enter username...'})
        self.fields['password1'].widget.attrs.update({'class':'form-control', 'placeholder': 'Enter password...'})
        self.fields['password2'].widget.attrs.update({'class':'form-control', 'placeholder': 'Confirm password...'})


class TrainingSessionForm(ModelForm, DateInput):
    input_type = 'date'
    class Meta:
        model = TrainingSession
        fields = ['date', 'time_trained', 'numRolls']
        widgets = {
            'date': DateInput(),
        }