from django.forms import ModelForm
from .models import *
from django import forms

class DateInput(forms.DateInput):
    input_type='date'

class Fees_form(ModelForm):
    class Meta:
        model =Fees
        types = [
            ('Class Fees', 'Class Fees'),
            ('Exam Fees', 'Exam Fees')
        ]
        fields = ('student','student_class','Fees_Amount','Fees_Type','Start_Date','end_Date')
        widgets={
            'Fees_Type':forms.Select(attrs={'class' : 'form-control'},choices=types),
            'Fees_Amount':forms.TextInput(attrs={'class' : 'form-control','type':'number'}),
            'Start_Date': forms.DateInput(attrs={'class':'form-control', 'placeholder':'Select a date','type':'date'}),
            'end_Date': forms.DateInput(attrs={'class':'form-control', 'placeholder':'Select a date','type':'date'}),
        }

