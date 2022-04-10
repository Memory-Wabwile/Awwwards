from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
#from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.TextField()
    image = CloudinaryField('images/' , default='')
    description =models.TextField()
    url=models.TextField()
    user= models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    #date = models.DateTimeField(default=timezone.now)
    def save_post(self):
        self.save()

    @classmethod
    def display_post(cls):
        post = cls.objects.all()
        return post

    @classmethod
    def delete_profile(cls,id):
        cls.objects.filter(id).delete()
    
    @classmethod
    def search_post(cls,searched):
        posts = cls.objects.filter(title__icontains=searched)
        return posts

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,default="")
    profilePhoto = CloudinaryField('images/' , default='')
    bio = models.TextField()
    contacts=models.TextField()
    projects=models.ForeignKey(Post,on_delete= models.CASCADE,null = True)


    def save_profile(self):
        self.save()

    @classmethod
    def delete_profile(cls,id):
        cls.objects.filter(id).delete()

    @classmethod
    def update_profile(cls,id,update_profile):
        cls.objects.filter(id).update(bio=update_profile)

    @classmethod
    def display_profile(cls):
        profile = cls.objects.all()
        return profile

    def __str__(self):
        return self.user

