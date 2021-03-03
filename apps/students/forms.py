from django.forms import ModelForm
from .models import *
from django import forms

class DateInput(forms.DateInput):
    input_type='date'

class StudentForm(ModelForm):
  class Meta:
    model = Students
    fields = ('full_name','father_name','mothers_name','gender',
    'date_of_birth','date_of_register','address','student_photo','Student_class',
    'student_parent','place_birth')
    GENDER = [
      ('Male', 'Male'),
      ('Female', 'Female')
    ]
    widgets={
      'full_name':forms.TextInput(attrs={'class' : 'form-control'}),
      'father_name':forms.TextInput(attrs={'class' : 'form-control'}),
      'mothers_name':forms.TextInput(attrs={'class' : 'form-control'}),
      'place_birth':forms.TextInput(attrs={'class' : 'form-control'}),
      'gender':forms.Select(attrs={'class' : 'form-control'},choices=GENDER),
      'date_of_birth': forms.DateInput(attrs={'class':'form-control', 'placeholder':'Select a date','type':'date'}),
      'date_of_register': forms.DateInput(attrs={'class':'form-control', 'placeholder':'Select a date','type':'date'}),
      'address':forms.Textarea(attrs={'class' : 'form-control',"rows":5})
    }

class Student_file_form(ModelForm):
  class Meta:
    model =Student_File
    exclude = ['student']
    widgets={
      'file_name':forms.TextInput(attrs={'class' : 'form-control'}),
    }

class editphotoform(forms.Form):
  photo=forms.ImageField() 