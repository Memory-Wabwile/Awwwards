from rest_framework import serializers
from .models import Profile , Post

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'profilePhoto', 'bio' , 'contacts', 'projects')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'image', 'description' , 'url' , 'user')