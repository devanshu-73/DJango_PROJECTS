from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(unique= True,max_length= 30)
    password = models.CharField(max_length= 20)
    role = models.CharField(max_length= 20) # chairman or society_member
    isActive = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return (self.role +" "+ self.email) 

class Chairman(models.Model):
    userid = models.ForeignKey(User,on_delete = models.CASCADE)
    firstname = models.CharField(max_length = 20)
    lastname = models.CharField(max_length = 10)
    contact = models.CharField(max_length = 10)
    blockno = models.CharField(max_length = 3)
    houseno = models.CharField(max_length = 4)
    
    def __str__(self):
        return (self.firstname +" | "+"Block : "+self.blockno+" | "+"House No : "+self.houseno) 
    
    