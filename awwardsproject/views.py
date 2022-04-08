from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .forms import ProfileForm
from .models import Profile

def index(request):

    return render(request, 'awwardsproject/index.html')



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
    form = ProfileForm(initial={'name':request.user.username, 'bio':'test'})

   
    return render(request, 'profile/edit.html', {'form': form})  


def profile(request):
    form = ProfileForm

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        Profile.objects.filter(id__gt=1)
        
        profile=Profile.objects.get(user= request.user.id)
       
        if form.is_valid():
            image=form.cleaned_data['image']   
            user=form.cleaned_data['user']  
                      
            profile=Profile(image,user)
            form.save()

            profile=Profile.objects.get(user= request.user.id)
            messages.success(request, 'Profile has been updated')

            return redirect ('/profile')
        else:
            return render(request, 'profile/edit.html', {'form': form})

    else:
        profile=Profile.objects.get(user_id= request.user)

        return render(request, 'profile/profile.html', {'form': form, 'profile':profile})         





