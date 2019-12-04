from django.shortcuts import render, render_to_response , get_object_or_404, HttpResponse
from .models import EventInfo
from django.views.generic import ListView, TemplateView


# Create your views here.

class Event_List_View(ListView):
    template_name = 'Event_Dashbord.html'
    model = EventInfo
    context_object_name = "events"

class Event_Creation(TemplateView):
    template_name = 'Event_Creation.html'

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
    
    return created_event(request, id)

def created_event(request, id): 
    return render_to_response('Created_Event.html', {
        'event' : get_object_or_404(EventInfo, id=id)
    })