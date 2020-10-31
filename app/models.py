from django.db import models
from django.contrib import auth

# Create your models here.

class Account(models.Model):
    name = models.CharField(max_length=1000)
    organisation = models.CharField(max_length=1000, blank=True, default="")
    phone = models.IntegerField(default=0)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    bio = models.CharField(max_length=1000, blank=True)