from django.db import models
from django.contrib.auth.models import User

class Group(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_groups')
    description = models.CharField(max_length=255)
    cover_image = models.ImageField(upload_to='profile_pictures', default='logo1.jpg')
    members = models.ManyToManyField(User, blank=True, related_name='group_members')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name




# class Discussion(models.Model):
#     group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='discussions')
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     title = models.CharField(max_length=255)
#     text = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)