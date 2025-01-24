from django.shortcuts import render, redirect
from .models import ChatRoom, Message
from django.contrib.auth.decorators import login_required


@login_required
def rooms(request):
    chat_rooms = ChatRoom.objects.all() 
    return render(request, 'room/rooms.html', {'chat_rooms': chat_rooms})


@login_required
@login_required  # Ensure the user is logged in
def room_detail(request, slug):
    room = ChatRoom.objects.get(slug=slug)
    
    if request.method == 'POST':
        content = request.POST.get('message')
        if content:
            Message.objects.create(room=room, user=request.user, content=content)
            return redirect('room_detail', slug=room.slug)  # Redirect to the same room after sending

    messages = room.messages.all()  # Fetch messages for the room
    return render(request, 'room/room_detail.html', {'room': room, 'messages': messages})