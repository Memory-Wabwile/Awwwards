from django.shortcuts import render
from .models import Post

# Create your views here.

def home (request):
    message = "Landing page"

    posts = Post.objects.all()
    return render (request , 'home.html' , {'message':message , 'posts':posts})

def details(request):
    message = "details page"

    return render (request , 'details.html' , {'message':message})

def profile(request):
    message = 'the profile page'

    return render(request , 'profile.html' , {'message':message})

def rate(request):
    message = "ratings page"

    return render(request, 'rate.html' , {'message':message})

def create_post(request):
    message= "create a post"

    return render(request , 'post.html' , {'message':message})

def updateProfile(request):
    message="update your profile"

    return render(request,'updateProfile.html' , {'message':message})

def search(request):
    message="search for an item"

    return render (request , 'search.html' , {'message':message})