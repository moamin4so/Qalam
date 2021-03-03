from django.db import models
from django.utils import timezone
# Create your models here.
class Parent(models.Model):
  GENDER = [
      ('Male', 'Male'),
      ('Female', 'Female')
  ]
  full_name           =models.CharField(max_length=200)
  gender              =models.CharField(max_length=10, choices=GENDER, default='Male')
  mobile_number       =models.CharField(max_length=20, blank=True)
  address             =models.TextField(blank=True)
  date_of_register    =models.DateField(default=timezone.now)
  def __str__(self):
    return self.full_name