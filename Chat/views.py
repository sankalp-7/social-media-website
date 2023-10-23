from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Room, Message
import collections
import heapq
def getlastmsg(room):
    lastMessage=Message.objects.filter(room=room).last()
    return lastMessage

@login_required
def rooms(request):
    rooms = Room.objects.all()
    room_data=[]
    for room in rooms:
        latest_msg=getlastmsg(room)
        room_data.append({
            'room': room,
            'latest_message': latest_msg,
        })
    
        
    room_data.sort(key=lambda x: x['latest_message'].date_added, reverse=True)
    print(room_data)
    return render(request, 'Chat/rooms.html', {'rooms': room_data})

@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]

    return render(request, 'Chat/room.html', {'room': room, 'messages': messages})

def mail(request):
    
    return render(request, 'Chat/rooms.html')
