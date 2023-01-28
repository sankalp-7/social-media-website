from django.urls import path
from.views import *
app_name='djinsta'

urlpatterns=[ 
    path('',home),
    path('signup/',signup,name='signup'),
    path('signin/',signin,name='signin'),
    path('logout/',signin,name='logout'),
]