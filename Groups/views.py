
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
from Post.models import *

@login_required
def create_group_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        cover_image = request.FILES.get('cover_image')
        user = request.user

        group = Group(name=name, description=description, cover_image=cover_image, created_by=user)
        group.save()

        # Add the creator as a member of the group
        group.members.add(user)

        # Redirect to the group's page
        return redirect('group-page', group_id=group.id)

    return render(request, 'Groups/create_group.html')

def group_home(request):
    user_profile = UserProfile.objects.get(user=request.user)
    profile = get_object_or_404(UserProfile,user=request.user)
    context = {'profile':profile,'user_profile':user_profile}
    return render(request,'Groups/group_home.html',context)



# def group_detail(request, group_id):
#     group = get_object_or_404(Group, id=group_id)
#     # discussions = Discussion.objects.filter(group=group)
#     return render(request, 'Groups/group_detail.html', {'group': group})


# def group_list(request):
#     groups = Group.objects.all()
#     context = {'groups':groups}
#     return render(request, 'Groups/group_list.html', context)

# def join_group(request, group_id):
#     group = get_object_or_404(Group, id=group_id)
#     group.members.add(request.user)
#     return redirect('group_detail', group_id=group_id)

# def leave_group(request, group_id):
#     group = get_object_or_404(Group, id=group_id)
#     group.members.remove(request.user)
#     return redirect('group_detail', group_id=group_id)

# def create_discussion(request, group_id):
#     group = get_object_or_404(Group, id=group_id)
#     if request.method == 'POST':
#         form = DiscussionForm(request.POST)
#         if form.is_valid():
#             discussion = form.save(commit=False)
#             discussion.group = group
#             discussion.author = request.user
#             discussion.save()
#             return redirect('group_detail', group_id=group_id)
#     else:
#         form = DiscussionForm()
#     return render(request, 'create_discussion.html', {'form': form, 'group': group})


