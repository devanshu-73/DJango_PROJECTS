from django.db import models

# Create your models here.

class User_details(models.Model):
    name = models.CharField(max_length=20)
    subjects = models.JSONField(default=list)
    gender = models.CharField(max_length=10)
 