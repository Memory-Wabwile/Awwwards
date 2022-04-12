from django.shortcuts import redirect, render
from .models import Post , Profile , Review
from django.contrib.auth.models import User
from .forms import newPost , RatingsForm , profileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer , PostSerializer
from rest_framework import status


# Create your views here.

def home (request):
    message = "Landing page"

    posts = Post.objects.all()
    return render (request , 'home.html' , {'message':message , 'posts':posts})

def details(request,id):
    message = "details page"

    posts = Post.objects.get(id=id)
    return render (request , 'details.html' , {'message':message , 'posts':posts})


@login_required(login_url='/accounts/login/')
def profile(request):
    message = 'the profile page'
    
    # posts = Post.objects.get(id=id)
    # profile = Profile.objects.get(id=id)
    return render(request , 'profile.html' , {'message':message})

@login_required(login_url='/accounts/login/')
def rate(request):
    message = "ratings page"
    
    # ratings = Review.objects.filter(user=request.user,id=id).first()
    # all_ratings = Review.objects.filter(id=id).all()
    # post = Post.objects.get(id = id)
    # user = request.user
    # if request.method == 'POST':
    #     form = RatingsForm(request.POST)
    #     if form.is_valid():
    #         rate = form.save(commit=False)
    #         rate.user = user
    #         rate.post = post
    #         rate.save()
    #         return redirect('home')
    # else:
    form = RatingsForm()
    return render(request,"rate.html",{"form":form,})
    
@login_required(login_url='/accounts/login/')
def updateProfile(request):
    message="update your profile"

    form = profileForm()
    return render(request,'updateProfile.html' , {'message':message , 'form':form})

def search(request):
   
    if 'postss' in request.GET and request.GET["postss"]:
        search_term = request.GET.get("postss")
        searched_postss = Post.search_post(search_term)
        message = f"{search_term}"
        return render(request, 'search.html',{"message":message,"searched_postss": searched_postss})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})


@login_required(login_url='/accounts/login/')
def create_post(request):
    current_user = request.user
    if request.method == "POST":
        form = newPost(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            title = form.cleaned_data["title"]
            image = form.cleaned_data["image"]
            description = form.cleaned_data["description"]
            url = form.cleaned_data["url"]
            user = current_user
            post = Post(
                title=title,
                image=image,
                description=description,
                url=url,
                user=user
            )
            post.save()
        return redirect("home")
    else:
        form = newPost()
    return render(request, "post.html", {"form": form})

@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('home')


class ProfileList(APIView):
    def get(self, request, format=None):
        all_profile = Profile.objects.all()
        serializers = ProfileSerializer(all_profile, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class PostList(APIView):
    def get(self, request, format=None):
        all_post = Post.objects.all()
        serializers = PostSerializer(all_post, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = PostSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    