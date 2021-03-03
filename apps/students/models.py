from django.db import models
from django.utils import timezone
from apps.parents.models import *
from apps.classes.models import *
# Create your models here.
class Students(models.Model):
  GENDER = [
      ('Male', 'Male'),
      ('Female', 'Female')
  ]
  full_name           =models.CharField(max_length=200)
  father_name         =models.CharField(max_length=200)
  mothers_name        =models.CharField(max_length=200)
  gender              =models.CharField(max_length=10, choices=GENDER, default='Male')
  address             =models.TextField(blank=True)
  place_birth         =models.CharField(max_length=200,blank=True)
  Student_class       =models.ManyToManyField(Classes)
  student_parent      =models.ForeignKey(Parent,null=True,on_delete=models.SET_NULL)
  date_of_birth       =models.DateField(default=timezone.now)
  date_of_register    =models.DateField(default=timezone.now)
  student_photo       =models.ImageField(blank=True)
  class Meta:
    verbose_name = "Student"
    verbose_name_plural = "Students"
  def __str__(self):
    return self.full_name


class Student_File(models.Model):
  student=models.ForeignKey(Students,null=True,on_delete=models.CASCADE)
  file_name=models.CharField(max_length=20)
  file_input=models.FileField()
  def __str__(self):
    return self.file_name