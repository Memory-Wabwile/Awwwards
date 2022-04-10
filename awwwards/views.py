from django.shortcuts import redirect, render
from .models import Post
from .forms import newPost

# Create your views here.

def home (request):
    message = "Landing page"

    posts = Post.objects.all()
    return render (request , 'home.html' , {'message':message , 'posts':posts})

def details(request,id):
    message = "details page"

    posts = Post.objects.get(id=id)
    return render (request , 'details.html' , {'message':message , 'posts':posts})

def profile(request):
    message = 'the profile page'

    return render(request , 'profile.html' , {'message':message})

def rate(request):
    message = "ratings page"

    return render(request, 'rate.html' , {'message':message})

def updateProfile(request):
    message="update your profile"

    return render(request,'updateProfile.html' , {'message':message})

def search(request):
   
    if 'postss' in request.GET and request.GET["postss"]:
        search_term = request.GET.get("postss")
        searched_postss = Post.search_post(search_term)
        message = f"{search_term}"
        return render(request, 'search.html',{"message":message,"searched_postss": searched_postss})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def create_post(request):
    current_user = request.user
    if request.method == "POST":
        form = newPost(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data["title"]
            image = form.cleaned_data["image"]
            description = form.cleaned_data["description"]
            url = form.cleaned_data["url"]
            post = Post(
                title=title,
                image=image,
                description=description,
                url=url,
            )
            post.save()
        return redirect("landingPage")
    else:
        form = newPost()
    return render(request, "post.html", {"form": form})