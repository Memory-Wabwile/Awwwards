from django.shortcuts import render

# Create your views here.

def home (request):
    message = "Landing page"
    return render (request , 'home.html' , {'message':message})

def details(request):
    message = "details page"

    return render (request , 'details.html' , {'message':message})