from django.db import models

# Create your models here.

class Account(models.Model):
    name = models.CharField(max_length=1000)
    organisation = models.CharField(max_length=1000, blank=True, default="")
    phone = models.IntegerField(default=0)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=1000, blank=True)