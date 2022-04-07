from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


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


