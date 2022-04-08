from django.shortcuts import render

# Create your views here.

def home (request):
    message = "Landing page"
    return render (request , 'home.html' , {'message':message})

def details(request):
    message = "details page"

    return render (request , 'details.html' , {'message':message})

def profile(request):
    message = 'the profile page'

    return render(request , 'profile.html' , {'message':message})

def rate(request):
    message = "ratings page"

    return render(request, 'rate.html' , {'message':message})