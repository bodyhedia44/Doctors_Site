from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    title=models.CharField(max_length=40,null=False,blank=False)
    image=models.ImageField(null=False,blank=False,upload_to='image_upload')
    time=models.DateTimeField(auto_now=True)
    content=models.TextField(null=False,blank=False)
    author=models.ForeignKey(User, on_delete=models.CASCADE, blank=True,related_name='author')
    like=models.ManyToManyField(User,blank=True,related_query_name='like')
    def __str__(self):
        return str(self.title)
