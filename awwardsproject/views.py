from email.mime import image
from unicodedata import name
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.db.models import Avg

from .forms import ProfileForm, PostForm
from .models import Post, Profile, Rating

def index(request):
    profile_form=ProfileForm
    post_form=PostForm
    post=Post.display()
    scale = range(1, 11)
    return render(request, 'awwardsproject/index.html', {'scale': scale, "posts":post, "profile_form":profile_form, "post_form":post_form})



# User registration 

def register(request):
    form = UserCreationForm

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User has been registered')

            return redirect ('/accounts/login')
        else:
            return render(request, 'registration/registration_form.html', {'form': form})

    else:
        return render(request, 'registration/registration_form.html', {'form': form})  


def editProfile(request):
    profile=Profile.objects.get(user= request.user.id)

    form = ProfileForm(initial={'name':profile.name, 'bio':profile.bio, 'email':profile.email})

   
    return render(request, 'profile/edit.html', {'form': form})  


def profile(request):
    form = ProfileForm

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        # Profile.objects.filter(id__gt=1)
        
        profile=Profile.objects.get(user= request.user.id)
       
        if form.is_valid():

            # print(request.FILES['image'])
            # print(form.cleaned_data['image'])


            profile.image=form.cleaned_data['image'] if len(request.FILES) != 0 else profile.image
            profile.name=form.cleaned_data['name']  
            profile.bio=form.cleaned_data['bio'] 
            profile.email=form.cleaned_data['email'] 

            # profile=Profile(image,name,bio)
            profile.save()

            # profile=Profile.objects.get(user= request.user.id)
            messages.success(request, 'Profile has been updated')

            return redirect ('/profile')
        else:
            return render(request, 'profile/edit.html', {'form': form})

    else:
        

        if Profile.objects.filter(user = request.user.id).count() == 0:
            profile = Profile(user=request.user, name=request.user.username, email=request.user.email, bio='')
            profile.save()
        else:
            profile= request.user.profile 
        return render(request, 'profile/profile.html', {'form': form, 'profile':profile})     

def viewPost(request, id):
    post = get_object_or_404(Post, pk=id)
    ratings = Rating.objects.filter(post = id)

    scale = range(1, 11)

    design_rating_obj = Rating.objects.filter(post = id, rating = 'design').aggregate(Avg('scale'))
    usability_rating_obj = Rating.objects.filter(post = id, rating = 'usability').aggregate(Avg('scale'))
    content_rating_obj = Rating.objects.filter(post = id, rating = 'content').aggregate(Avg('scale'))

    if design_rating_obj['scale__avg'] is not None:
        design_rating = round(design_rating_obj['scale__avg'])
    else:
        design_rating = 0

    if usability_rating_obj['scale__avg'] is not None:
        usability_rating = round(usability_rating_obj['scale__avg'])
    else:
        usability_rating = 0

    if content_rating_obj['scale__avg'] is not None:
        content_rating = round(content_rating_obj['scale__avg'])
    else:
        content_rating = 0

    post.design_rating = design_rating
    post.usability_rating = usability_rating
    post.content_rating = content_rating
    post.save()

    return render(request, 'awwardsproject/show.html', {
        'post': post,
        'scale': scale,
        'design_rating': design_rating,
        'usability_rating': usability_rating,
        'content_rating': content_rating,
        'ratings': ratings
    })   

def storeRating(request, rating, post_id, scale):

    rating = Rating(rating=rating, scale=scale, post=get_object_or_404(Post, pk=post_id), user=request.user)
    rating.save()


    return redirect('/view-post/' + str(post_id))

def post(request):
    form = PostForm
    current_user = request.user
    if request.method == 'POST':
        print(request.POST['post'])
        form = PostForm(request.POST, request.FILES)
        
        if form.is_valid():
            post = Post()
            post.title = form.cleaned_data['title']
            post.post = form.cleaned_data['post']
            post.author = current_user
            post.projecturl= form.cleaned_data['projecturl']
            post.picture = form.cleaned_data['picture']
            post.save()
            messages.success(request, 'Posted')

            return redirect ('index')
        else:
            return render(request, 'post/new_post.html', {'form': form})

    else:
        return render(request, 'post/new_post.html', {'form': form})             





