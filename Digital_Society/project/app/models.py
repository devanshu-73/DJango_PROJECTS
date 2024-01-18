from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(unique=True,max_length=35)
    password = models.CharField(max_length=20)
    role = models.CharField(max_length=20)  #chairman / societymember
    isActive = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now=True)

class Chairman(models.Model):
    userid = models.ForeignKey(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length = 20)
    lastname = models.CharField(max_length=20)
    contact = models.CharField(max_length=11)
    blockno = models.CharField(max_length=3)
    houseno = models.CharField(max_length=4)
    pic = models.FileField(upload_to="media/upload",default="default.png")

class Member(models.Model):
    userid = models.ForeignKey(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length = 20)
    lastname = models.CharField(max_length=20)
    contact = models.CharField(max_length=11)
    blockno = models.CharField(max_length=3)
    houseno = models.CharField(max_length=4)
    occupation = models.CharField(max_length=20)
    job_address = models.TextField()
    bloodgroup = models.CharField(max_length=3)
    vehical_details = models.CharField(max_length=20)
    pic = models.FileField(upload_to="media/upload",default="default.png")


class Notice(models.Model):
    notice_title = models.CharField(max_length=50)
    notice_description = models.TextField()
    pic = models.FileField(upload_to="upload",null=True,blank=True)
    video = models.FileField(upload_to="videos",verbose_name="noticeclip",blank=True,null=True)
    created_at = models.DateTimeField(auto_now=True)



    