from django.urls import path
from . import views

app_name = 'Post'

urlpatterns = [
    path('',views.home, name='home'),
    path('profile/<str:username>/',views.profile,name='profile'),
    path('create_post/', views.create_post, name='create_post'),
    path('like_post/<int:pk>/', views.like_post, name='like_post'),
    path('settings/',views.settings, name='settings'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('posts/<int:pk>/comment/', views.create_comment, name='create_comment'),
    path('follow/<str:username>/',views.follow,name='follow'),
    path('unfollow/<str:username>/',views.unfollow,name='unfollow'),
    # path('create_comment/<int:pk>/', views.create_comment, name='create_comment'),
]