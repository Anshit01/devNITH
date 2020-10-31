from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Account(models.Model):
    name = models.CharField(max_length=1000)
    organisation = models.CharField(max_length=1000, blank=True, default="")
    phone = models.IntegerField(default=0)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=1000, blank=True)

class InternshipPost(models.Model):
    recruiter = models.ForeignKey(Account, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    posted_on = models.DateField()
    last_date = models.DateField()
    tags = ArrayField(models.CharField(max_length=50), blank=True)
    description = models.TextField()
    registration_link = models.CharField(max_length=1000)

class OpenSourcePost(models.Model):
    maintainer = models.ForeignKey(Account, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    posted_on = models.DateField()
    last_date = models.DateField()
    tags = ArrayField(models.CharField(max_length=50), blank=True)
    description = models.TextField()
    registration_link = models.CharField(max_length=1000)