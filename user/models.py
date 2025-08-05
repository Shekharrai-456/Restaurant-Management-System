from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
   phone = models.CharField(max_length=13, null=True, blank =True, unique=True)
   
   USERNAME_FIELD = 'phone'
   REQUIRED_FIELDS = ['first_name','last_name']
   
   def __str__(self):
      return f"{self.phone}"