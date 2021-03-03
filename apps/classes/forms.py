from django.forms import ModelForm
from .models import *
from django import forms

class Class_Form(ModelForm):
  class Meta:
    model = Classes
    fields=('name',)
    widgets={
      'name':forms.TextInput(attrs={'class' : 'form-control'}),
    }