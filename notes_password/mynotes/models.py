from django.contrib.auth.models import AbstractUser,User
from django.db import models
import datetime

#username, email, password, 
class User(AbstractUser):
    pass
# Create your models here.
class Notes(models.Model):
    content=models.TextField(max_length=10000)
    Title=models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.id}-{self.Title}"

class Fnote(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="Mynotes")
    files=models.OneToOneField(Notes,on_delete=models.CASCADE,null=True,related_name="files")
    
    def __str__(self):
        return f"{self.user}-{self.files}"
