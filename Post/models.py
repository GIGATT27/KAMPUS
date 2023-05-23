from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=500, blank=True)
    profileimg = models.ImageField(upload_to='profile_pictures', default='logo1.jpg')
    website_url = models.URLField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    following = models.ManyToManyField(User, blank=True, related_name='followed_by', symmetrical=False)

    def __str__(self):
        return f'{self.user.username}'

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(blank=True,null=True, upload_to='post_images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)

    def __str__(self):
        return f'{self.user.username}: {self.content[:50]}'


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.content[:50]}'
    
class Follower(models.Model):
    follower = models.ForeignKey(UserProfile, related_name='followed_by', on_delete=models.CASCADE)
    followed = models.ForeignKey(UserProfile, related_name='followers', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('follower', 'followed')