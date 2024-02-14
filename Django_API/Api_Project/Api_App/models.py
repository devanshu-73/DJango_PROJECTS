from django.db import models

# Create your models here.
class Form(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField(unique = True,max_length = 50)
    password = models.CharField(max_length = 20)
    isActive = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name
    