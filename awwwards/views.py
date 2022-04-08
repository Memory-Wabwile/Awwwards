from django.shortcuts import render

# Create your views here.

def home (request):
    message = "Landing page"
    return render (request , 'home.html' , {'message':message})