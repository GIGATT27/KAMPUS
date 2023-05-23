
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.db.models import Q
from Post.models import *

# Create your views here.


def signup(request):
    if request.method == 'POST':
        # first_name = request.POST['first_name']
        # last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used') 
                return redirect('')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username Already taken')
                return redirect('')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                # log user in and direct to settings page later 
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request,user_login)

                # New profile for new User 
                user_model = User.objects.get(username=username)
                new_profile = UserProfile.objects.create(user=user_model)
                new_profile.save()
                return redirect('Post:settings')
        else:
            messages.info(request,'Password Not Matching')
            return redirect('Users:signup')
   
    else:
        return render(request, 'Users/signup.html')
    context = {}
    return render(request,'Users/signup.html',context)
    
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('Post:home')
        else:
            messages.info(request,'User does not exist!')
            return redirect('Users:signin')
    else:
        return render(request,'Users/signin.html')

@login_required
def signout(request):
    logout(request)
    return redirect('Users:signin')