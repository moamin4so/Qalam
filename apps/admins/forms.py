from django.forms import ModelForm
from .models import *
from django import forms

class AdminForm(ModelForm):
  class Meta:
    model = AdminsDB
    exclude = ['user']
    widgets={
      'full_name':forms.TextInput(attrs={'class' : 'form-control'}),
      'username':forms.TextInput(attrs={'class' : 'form-control'}),
      'password':forms.TextInput(attrs={'class' : 'form-control','type':'text'}),
      'Email':forms.TextInput(attrs={'class' : 'form-control' ,'type':'email'}),
    }