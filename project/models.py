from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from django.db.models import Q

# Create your models here.
class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture =models.ImageField(upload_to= 'profiles/', blank=True, default="profiles/a.jpg")
    bio = models.CharField(max_length=100, default='Welcome to you bio')
    contact = models.CharField(max_length=80)

    def _str_(self):
        return self.bio

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def update_bio(cls,id, bio):
        update_profile = cls.objects.filter(id = id).update(bio = bio)
        return update_profile

    @classmethod
    def get_all_profiles(cls):
        profile = Profile.objects.all()
        return profile
    @classmethod
    def search_user(cls,user):
        return cls.objects.filter(user_username_icontains=user).all()

class Post(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', default='')
    description = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now=True)
    link = models.URLField(max_length=250)
    country = models.CharField(max_length=50)

    

    def _str_(self):
        return self.title
    
    class Meta:
        ordering = ['-date_posted']

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    @classmethod
    def search(cls,searchterm):
        search = Post.objects.filter(Q(title_icontains=searchterm)|Q(description_icontains=searchterm)|Q(country_icontains=searchterm))
        return search

class Rating(models.Model):
    rating = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    )
    design = models.IntegerField(choices=rating,blank=True,default=0)
    usability = models.IntegerField(choices=rating,blank=True,default=0)
    creativity = models.IntegerField(choices=rating,blank=True,default=0)
    content = models.IntegerField(choices=rating,blank=True,default=0)
    overall_score = models.IntegerField(blank=True,default=0)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)

    def save_rating(self):
        self.save()

    def _str_(self):
        return f'{self.post} Rating'