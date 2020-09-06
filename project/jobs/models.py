from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Doctor(models.Model):
    name=models.CharField(max_length=20,null=False,blank=False)
    subtitle=models.CharField(max_length=20,null=False,blank=False)
    address=models.CharField(max_length=20,null=False,blank=False)
    price=models.IntegerField(null=False,blank=False)
    wait=models.IntegerField(null=False,blank=False)
    work=models.IntegerField(null=False,blank=False)
    phone=models.IntegerField(null=False,blank=False)
    info=models.TextField(null=False,blank=False)
    prof_pic=models.ImageField(null=False,blank=False,upload_to='image_upload')
    choice=models.CharField(max_length=80)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True,primary_key=True)
    
    def __str__(self):
        return str(self.name)


class Comment(models.Model):
    name=models.CharField(max_length=20)
    comment=models.TextField()
    where=models.CharField(max_length=300)

def __str__(self):
        return str(self.comment)

