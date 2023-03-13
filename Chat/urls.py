from django.urls import path

from.views import *

urlpatterns = [
    path('', rooms, name='rooms'),
    path('<slug:slug>/',room, name='room'),
]