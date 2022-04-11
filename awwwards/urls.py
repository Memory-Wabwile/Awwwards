from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('details/<id>/' , views.details , name="details"),
    path('profile/' , views.profile , name="profile"),
    path('rate/' , views.rate , name="rate"),
    path('post/', views.create_post, name = 'post'),
    path('updateProfile/' , views.updateProfile , name ='updateProfile'),
    path('search/', views.search , name ="search"),
     path('logout/', views.logout_user, name='logout'),
]