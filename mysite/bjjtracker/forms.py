from dataclasses import fields
from django.forms import ModelForm
from .models import *

class TechniqueForm(ModelForm):

    class Meta:
        model = Technique
        fields = '__all__'
        exclude = ['id']

