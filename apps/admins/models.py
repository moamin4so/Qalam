from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here

class AdminsDB(models.Model):
    full_name           =models.CharField(max_length=200)
    username            =models.CharField(max_length=200)
    password            =models.CharField(max_length=200)  
    Email               =models.CharField(max_length=200) 
    user                =models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.full_name      