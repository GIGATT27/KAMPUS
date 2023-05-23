from django.urls import path
from . import views
from Groups.views import *

app_name = 'Groups'

urlpatterns = [
    # path('group_list/', views.group_list, name='group_list'),
    # path('group_detail/<int:group_id>/',views.group_detail,name='group_detail'),
    path('groups/create/', views.create_group_view, name='create_group_view'),
    path('group/home/',views.group_home,name='group_home'),
]