from django.forms import ModelForm
from .models import *
from django import forms

class DateInput(forms.DateInput):
    input_type='date'

class TeacherForm(ModelForm):
  class Meta:
    model = Teacher
    fields = ('full_name','mobile_number','gender','date_of_birth','date_of_register','address','image')
    GENDER = [
      ('Male', 'Male'),
      ('Female', 'Female')
    ]
    widgets={
      'full_name':forms.TextInput(attrs={'class' : 'form-control'}),
      'mobile_number':forms.TextInput(attrs={'class' : 'form-control','type':'number'}),
      'gender':forms.Select(attrs={'class' : 'form-control'},choices=GENDER),
      'date_of_birth': forms.DateInput(attrs={'class':'form-control', 'placeholder':'Select a date','type':'date'}),
      'date_of_register': forms.DateInput(attrs={'class':'form-control', 'placeholder':'Select a date','type':'date'}),
      'address':forms.Textarea(attrs={'class' : 'form-control',"rows":5})
    }

class Teacher_file_form(ModelForm):
  class Meta:
    model =Teacher_File
    exclude = ['teacher']
    widgets={
      'file_name':forms.TextInput(attrs={'class' : 'form-control'}),
    }

class editphotoform(forms.Form):
  photo=forms.ImageField() 