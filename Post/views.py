from django.shortcuts import render,redirect,get_object_or_404
from . models import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.db.models import Q
from django.http import JsonResponse

@login_required
def create_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        content = request.POST['content']
        comment = Comment.objects.create(user=request.user, post=post, content=content)
        # return redirect('Post:post_detail', pk=post.pk)
        return redirect('Post:home')

@login_required
def post_detail(request, pk):
    user_profile = UserProfile.objects.get(user=request.user)
    profile = get_object_or_404(UserProfile,user=request.user)
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post).order_by('-created_at')
    if request.method == 'POST':
        content = request.POST['content']
        comment = Comment.objects.create(user=request.user, post=post, content=content)
        return redirect('Post:post_detail', pk=post.pk)

    context = {'post': post, 'comments': comments,'user_profile':user_profile,'profile':profile}
    return render(request, 'Post/post_detail.html', context)

@login_required
def create_post(request):
    if request.method == 'POST':
        content = request.POST['content']
        image = request.FILES.get('image')
        post = Post.objects.create(user=request.user, content=content, image=image)
        return redirect('Post:home')

@login_required
def like_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'like':
            post.likes.add(request.user)
        elif action == 'unlike':
            post.likes.remove(request.user)
        like_count = post.likes.count()
        already_liked = post.likes.filter(id=request.user.id).exists()
        data = {
            'success': True,
            'like_count': like_count,
            'already_liked': already_liked
        }
        return JsonResponse(data)
    else:
        return redirect('Post:home')

@login_required
def profile(request,username):
    profile = get_object_or_404(UserProfile,user__username=username)
    userProfile = UserProfile.objects.get(user__username=username)
    user_profile = UserProfile.objects.get(user=request.user)

    is_own_profile = (request.user == profile.user)
    current_user_follows = False 
    if request.user.is_authenticated:
        current_user_follows = Follower.objects.filter(follower=request.user.userprofile,followed=profile).exists() 

    context = {'profile':profile,'userProfile':userProfile,'user_profile':user_profile,'is_own_profile':is_own_profile,'current_user_follows':current_user_follows}
    return render(request,'Post/profile.html',context)

@login_required
def follow(request,username):
    user = request.user.userprofile
    profile = get_object_or_404(UserProfile,user__username=username)
    follower,created = Follower.objects.get_or_create(follower=user,followed=profile)
    user.following.add(request.user)
    return redirect('Post:profile',username=username)

@login_required
def unfollow(request,username):
    user = request.user 
    profile = get_object_or_404(UserProfile,user__username=username)
    followed_user = get_object_or_404(UserProfile,user__username=username)
    follow = Follower.objects.filter(follower=request.user.userprofile,followed=followed_user).first()

    if follow:
        follow.delete()
        return redirect('Post:profile',username=username)


@login_required
def settings(request):
    user_profile = UserProfile.objects.get(user=request.user)
    profile = get_object_or_404(UserProfile,user=request.user)

    if request.method == 'POST':

        if request.FILES.get('image') == None:
            image = user_profile.profileimg
            bio = request.POST['bio']
            location = request.POST['location']
        
            user_profile.profileimg = image 
            user_profile.bio = bio 
            user_profile.location = location 
            user_profile.save()

        if request.FILES.get('image') != None:
            image = request.FILES.get('image')
            bio = request.POST['bio']
            location = request.POST['location']

            user_profile.profileimg = image 
            user_profile.bio = bio 
            user_profile.location = location 
            user_profile.save()
        return redirect('Post:settings')

    context = {'user_profile':user_profile,'profile':profile}
    return render(request, 'Post/settings.html', context)

@login_required
def home(request):
    user_profile = UserProfile.objects.get(user=request.user)
    profile = get_object_or_404(UserProfile,user=request.user)
    posts = Post.objects.all().order_by('-created_at')
    context = {
        'profile':profile,
        'posts':posts,
        'user_profile':user_profile
    }
    return render(request,'Post/home.html',context)