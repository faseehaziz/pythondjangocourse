from tokenize import Name
from django.db import models

# Create your models here.

class Registration(models.Model):
    name = models.CharField(max_length = 30)
    password = models.CharField(max_length = 20)
    email = models.EmailField(unique = True)
    phone = models.BigIntegerField(unique = True)
    address = models.TextField()