from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Classes(models.Model):
  name = models.CharField(max_length=200, unique=True)
  class Meta:
    verbose_name = "Class"
    verbose_name_plural = "Classes"
    ordering = ['name']
  def __str__(self):
    return self.name