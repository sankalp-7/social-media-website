from django.urls import path,include
from.views import *
import notifications.urls
app_name='djinsta'

urlpatterns=[
    path('',home),
    path('signup/',signup,name='signup'),
    path('signin/',signin,name='signin'),
    path('logout/',signin,name='logout'),
    path('settings/',settings,name='settings'),
    path('profile/',profile,name='profile'),
    path('follow/<int:pk>',follow,name='follow'),
    path('unfollow/<int:pk>',unfollow,name='unfollow'),
    path('like/<str:pid>',like_post,name='likepost'),
    path('profile/<int:pk>',profile,name='profile'),
    path('deleteN/<int:pk>',delete_notification,name='deleteN'),
    path('search/',search_user,name='search_user'),
    path('comment/',comment, name='add_comment'),

]