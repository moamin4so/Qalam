from django.db import models
from django.utils import timezone

# Create your models here.
class Teacher(models.Model):
  GENDER = [
      ('Male', 'Male'),
      ('Female', 'Female')
  ]
  full_name           =models.CharField(max_length=200)
  gender              = models.CharField(max_length=10, choices=GENDER, default='Male')
  mobile_number       = models.CharField(max_length=20, blank=True)
  date_of_birth       = models.DateField(default=timezone.now)
  date_of_register    = models.DateField(default=timezone.now)
  address             = models.TextField(blank=True)
  image               =models.ImageField(blank=True)
  def __str__(self):
    return self.full_name


class Teacher_File(models.Model):
  teacher=models.ForeignKey(Teacher,null=True,on_delete=models.CASCADE)
  file_name=models.CharField(max_length=20)
  file_input=models.FileField()
  def __str__(self):
    return self.file_name