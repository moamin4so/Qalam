from django.forms import ModelForm
from .models import *
from django import forms

class DateInput(forms.DateInput):
    input_type='date'
    
class ParentForm(ModelForm):
  class Meta:
    model = Parent
    fields = ('full_name','gender','mobile_number','address','date_of_register')
    GENDER = [
      ('Male', 'Male'),
      ('Female', 'Female')
    ]
    widgets={
      'full_name':forms.TextInput(attrs={'class' : 'form-control'}),
      'mobile_number':forms.TextInput(attrs={'class' : 'form-control','type':'number'}),
      'gender':forms.Select(attrs={'class' : 'form-control'},choices=GENDER),
      'date_of_register': forms.DateInput(attrs={'class':'form-control', 'placeholder':'Select a date','type':'date'}),
      'address':forms.Textarea(attrs={'class' : 'form-control',"rows":5}),
    }