from django import forms
from .models import Post,Profile,Review,RATE_CHOICES

class newPost(forms.Form):
    title = forms.CharField(max_length=200)
    image = forms.ImageField()
    description = forms.CharField(max_length=200)
    url = forms.CharField(max_length=200)

class RatingsForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['design','usability','content']  

class profileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [ 'photo', 'bio']        
           