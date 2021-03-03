from django.db import models
from apps.classes.models import *
from apps.students.models import *
from django.utils import timezone
# Create your models here.

class Fees(models.Model):
  types = [
      ('Class Fees', 'Class Fees'),
      ('Exam Fees', 'Exam Fees')
  ]
  student      =models.ForeignKey(Students,null=True,on_delete=models.CASCADE)
  student_class=models.ForeignKey(Classes,null=True,on_delete=models.CASCADE)
  Fees_Amount  =models.FloatField()
  Fees_Type    =models.CharField(max_length=10, choices=types, default='Class Fees')
  Start_Date   =models.DateField(default=timezone.now)
  end_Date     =models.DateField(default=timezone.now)
  def __str__(self):
    return str(self.student)