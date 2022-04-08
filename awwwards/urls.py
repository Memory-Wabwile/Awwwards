from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('details/' , views.details , name="details"),
    path('profile/' , views.profile , name="profile"),
    path('rate/' , views.rate , name="rate"),

]