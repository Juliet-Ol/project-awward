from dataclasses import fields
from django import forms
from .models import Profile, Post, Rating

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude =['user']
        fields = '__all__'


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['author', 'published_date']
        fields = '__all__'  

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        exclude =['user', 'post']
        fields = '__all__'               