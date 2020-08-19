from django import forms
from .models import Profile, Post, Rating

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude=["user"]
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = []
class RatingsForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['design', 'usability', 'content','creativity']
        exclude=['overall_score','profile','post']