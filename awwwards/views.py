from django.shortcuts import render
from .models import Post
from .forms import newPost

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
   
    if 'postss' in request.GET and request.GET["postss"]:
        search_term = request.GET.get("postss")
        searched_postss = Post.search_post(search_term)
        message = f"{search_term}"
        return render(request, 'search.html',{"message":message,"searched_postss": searched_postss})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def new_post(request):
    current_user = request.user
    if request.method == "POST":
        form = newPost(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data["title"]
            project_image = form.cleaned_data["project_image"]
            description = form.cleaned_data["description"]
            url = form.cleaned_data["url"]
            post = Post(
                title=title,
                project_image=project_image,
                description=description,
                url=url,
            )
            post.save()
        return redirect("landingPage")
    else:
        form = newPost()
    return render(request, "new_post.html", {"postForm": form})