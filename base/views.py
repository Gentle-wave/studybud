from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Room

# Create your views here.


def home(request):
    rooms = list(Room.objects.values())  # Convert queryset to list of dictionaries
    return JsonResponse(rooms, safe=False)

def room(request):
    return render(request, 'room.html')
