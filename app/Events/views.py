from django.shortcuts import render, render_to_response , get_object_or_404, HttpResponse
from .models import EventInfo


# Create your views here.
def index(request):
    events = EventInfo.objects.all()
    return render(request, 'Event_Dashbord.html', {'events' : events})

def event_creation(request):
    return render(request, 'Event_Creation.html')

def event_creation_post(request):
    EventName =  request.POST["EventName"]
    slug = request.POST["slug"]
    EventDescription =  request.POST["EventDescription"]
    EventLocation =  request.POST["EventLocation"]
    NoofAttendees =  request.POST["NoofAttendees"]
    EventDate = request.POST["EventDate"]
    eventinfo = EventInfo()
    eventinfo.EventName=EventName
    eventinfo.slug = slug
    eventinfo.EventDescription=EventDescription
    eventinfo.EventLocation=EventLocation
    eventinfo.NoofAttendees=NoofAttendees
    eventinfo.EventDate=EventDate
    print("before saving")
    eventinfo.save()
    print("after")
    
    return HttpResponse("Page Created")
    #events = EventInfo.objects.all()
    #return render(request, 'Event_Dashbord.html', {'events' : events})

def created_event(request, id): 
    return render_to_response('Created_Event.html', {
        'event' : get_object_or_404(EventInfo, id=id)
    })