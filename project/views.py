from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Profile, Post, Rating
import datetime as dt
from . forms import ProfileForm, PostForm, RatingsForm

# Create your views here.
def index(request):
    date =dt.date.today()
    posts = Post.objects.all()
    return render(request, 'index.html', {"date":date, "posts":posts })

@login_required(login_url='/accounts/login/?next=/')
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user=current_user).first()
    posts = request.user.post_set.all()

    return render(request, 'profile.html', locals())

@login_required(login_url='/accounts/login/?next=/')
def updateprofile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            add = form.save(commit=False)
            add.user = current_user
            add.save()
            return redirect('profile')
    else:
        form = ProfileForm()
    return render(request, 'profile_update.html',{"form":form })

@login_required(login_url='/accounts/login/?next=/')
def new_post(request):
        current_user = request.user
        if request.method == 'POST':
                form = PostForm(request.POST, request.FILES)
                if form.is_valid():
                        add=form.save(commit=False)
                        add.user = current_user
                        add.save()
                return redirect('index')
        else:
                form = PostForm()
                return render(request,'new_post.html', {"form":form})


def search_results(request):

    if 'post' in request.GET and request.GET["post"]:
        search_term = request.GET.get("post")
        searched_posts = Post.search(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"posts": searched_posts})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def site(request,site_id):
    current_user = request.user
    profile = Profile.objects.filter(user=current_user).first()

    try:
        post= Post.objects.get(id=site_id)
    except:
        raise ObjectDoesNotExist()

    try:
        ratings = Rating.objects.filter(post_id=site_id)
        design = Rating.objects.filter(post_id=site_id).values_list('design',flat=True)
        usability = Rating.objects.filter(post_id=site_id).values_list('usability',flat=True)
        creativity = Rating.objects.filter(post_id=site_id).values_list('creativity',flat=True)
        content = Rating.objects.filter(post_id=site_id).values_list('content',flat=True)
        total_design=0
        total_usability=0
        total_creativity=0
        total_content = 0

        for rate in design:
            total_design+=rate

        for rate in usability:
            total_usability+=rate

        for rate in creativity:
            total_creativity+=rate

        for rate in content:
            total_content+=rate

        overall_score=(total_design+total_content+total_usability+total_creativity)/4

        post.design = total_design
        post.usability = total_usability
        post.creativity = total_creativity
        post.content = total_content
        post.overall_score = overall_score

        post.save()

    except:
        return None

    if request.method =='POST':
        form = RatingsForm(request.POST,request.FILES)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.post= post
            rating.profile = profile
            rating.overall_score = (rating.design+rating.usability+rating.creativity+rating.content)/2
            rating.save()
    else:
        form = RatingsForm()

    return render(request,"site.html",{"post":post,"profile":profile,"ratings":ratings,"form":form})