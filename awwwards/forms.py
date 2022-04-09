from django import forms

class newPost(forms.Form):
    title = forms.CharField(max_length=200)
    image = forms.ImageField()
    description = forms.CharField(max_length=200)
    url = forms.CharField(max_length=200)