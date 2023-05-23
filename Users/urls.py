from django.urls import path
from . import views
from Post.views import *

app_name = 'Users'

urlpatterns = [
    path('signout',views.signout,name='signout'),
    path('signup/',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
]