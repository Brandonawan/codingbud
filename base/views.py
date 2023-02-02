from django.shortcuts import render
from django.http import HttpResponse
from . models import Room
from .forms import RoomForm

# rooms = [
#     {'id': 1, 'name': 'lets learn python' },
#     {'id': 2, 'name': 'lets django' },
#     {'id': 3, 'name': 'Frontend Devs' },
# ]

rooms = Room.objects.all()
# .values()
# Create your views here. 
def home(request):
    return render(request, "base/home.html", {'rooms':rooms})

def room(request, id):
    # room = None
    # for i in rooms:
    #     if i['id'] == int(id):
    #         room = i 
    room = Room.objects.get(id=id)
    return render(request, 'base/room.html', {'room':room})

def createRoom(request):
    form = RoomForm()
    return render(request, 'base/room_form.html', {'form':form} )
