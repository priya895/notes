from pickle import TRUE
from django.contrib.auth.models import AbstractUser,User
from django.db import models
import datetime

#username, email, password, 
class User(AbstractUser):
    pass
    def __str__(self):
        return f"{self.id}-{self.username} - {self.email}"
# Create your models here.
class Notes(models.Model):
    content=models.TextField(max_length=10000)
    Title=models.CharField(max_length=64)
    owner= models.ForeignKey(User,on_delete=models.CASCADE,related_name="Owner",null=True)
    passwor= models.BooleanField(default = False)
    def __str__(self):
        return f"{self.id}-{self.Title}"
class Fpass(models.Model):
    ftitle=models.CharField(max_length=64)
    fpass=models.CharField(max_length=64)
    fuser=models.ForeignKey(User,on_delete=models.CASCADE,related_name="fuser",null=True)
    Fwish=models.BooleanField(default= False)
   
    def __str__(self):
        return f"{self.id}-{self.ftitle}"