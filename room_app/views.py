from django.shortcuts import render
from . form import Room_detailsForm
from . models import Room_details
from django.contrib import messages
# Create your views here.

def rooms(request):
    object = Room_details.objects.all()
    counter = Room_details.objects.count()
    context = {
        "object": object,
        "counter": counter
    }
    return render(request, 'room.html', context)

def create_room(request):
    fom = Room_detailsForm()
    if request.method == "POST":
        fom = Room_detailsForm(request.POST)
        if fom.is_valid():
            host = fom.cleaned_data["host"]
            room_name = fom.cleaned_data["room_name"]
            topic = fom.cleaned_data["topic"]
            room_description = fom.cleaned_data["room_description"]
            fom.save()
            messages.success(request, 'You have created a new room. You can now post')
        else:
            form = Room_detailsForm()
    context = {
        "fom":fom
    }
    return render(request, "create_room.html", context)


def browse_topics(request):
    obj = Room_details.objects.all()
    context = {
        "obj": obj
    }
    return render(request, "topics.html", context)

def recent_activity(request):
    obj = Room_details.objects.all()[:2]
    context = {
        "obj": obj
    }
    return render(request, "recent_activity.html", context)

def delete_room(request, pk):
    room = Room_details.objects.get(id=pk)
    if request.method == "POST":
        room.delete()
        messages.success(request, "Room deleted")
    context = {
        "room":room
    }
    return render(request, "delete_room.html", context)