from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Post(models.Model):
    title = models.CharField()
    image = CloudinaryField('images/' , default='')
    description =models.TextField()
    url=models.CharField()
    user= models.OneToOneField(User,on_delete=models.CASCADE,default="")


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,default="")
    profilePhoto = CloudinaryField('images/' , default='')
    bio = models.TextField()
    contacts=models.TextField()
    projects=models.ForeignKey(Post,on_delete= models.CASCADE,null = True)



