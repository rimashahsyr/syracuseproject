from django.shortcuts import render
from .models import EventInfo


# Create your views here.
def event_creation(request):
    return render(request, 'Event_Creation.html')

def event_creation_post(request):
    EventName =  request.POST["EventName"]
    EventDescription =  request.POST["EventDescription"]
    EventLocation =  request.POST["EventLocation"]
    NoofAttendees =  request.POST["NoofAttendees"]
    EventDate = request.POST["EventDate"]
    eventinfo = EventInfo()
    eventinfo.EventName=EventName
    eventinfo.EventDescription=EventDescription
    eventinfo.EventLocation=EventLocation
    eventinfo.NoofAttendees=NoofAttendees
    eventinfo.EventDate=EventDate
    print("before saving")
    eventinfo.save()
    print("after")
    return render(request, "Event_Creation.html")
