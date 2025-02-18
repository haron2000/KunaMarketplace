from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import ChatRoom, Message

@login_required
def chat_list(request):
    if request.user.is_business:
        chat_rooms = ChatRoom.objects.filter(business__owner=request.user)
    else:
        chat_rooms = ChatRoom.objects.filter(user=request.user)
    
    return render(request, 'chat/chat_list.html', {'chat_rooms': chat_rooms})

@login_required
def chat_room(request, room_id):
    chat_room = get_object_or_404(ChatRoom, id=room_id)
    messages = Message.objects.filter(room=chat_room).order_by('timestamp')
    
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Message.objects.create(room=chat_room, sender=request.user, content=content)
    
    return render(request, 'chat/chat_room.html', {
        'chat_room': chat_room,
        'messages': messages
    })
