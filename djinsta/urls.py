from django.urls import path
from.views import *
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
    path('like/<str:pid>',like_post,name='likepost')
]