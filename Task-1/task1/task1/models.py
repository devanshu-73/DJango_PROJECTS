from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=20)
    subject = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
 