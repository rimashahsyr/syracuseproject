from django.shortcuts import render, render_to_response , get_object_or_404, HttpResponse
from .models import EventInfo
from django.views.generic import ListView, TemplateView
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.views import View
from Profile.models import ProfileInfo


# Create your views here.

class Event_List_View(ListView):
    template_name = 'Event_Dashbord.html'
    model = EventInfo
    context_object_name = "events"

class Event_Creation(TemplateView):
    template_name = 'Event_Creation.html'

""" class Event_Creation_Post(View):
    def get(self, request):
        EventName =  request.POST["EventName"]
        EventDescription =  request.POST["EventDescription"]
        EventLocation =  request.POST.getlist('EventLocation')
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
        events = EventInfo.objects.all()
        return render(request, 'Event_Dashbord.html', {'events' : events}) """

def event_creation_post(request):
    EventName =  request.POST["EventName"]
    EventDescription =  request.POST["EventDescription"]
    EventLocation =  request.POST.getlist('EventLocation')
    NoofAttendees =  request.POST["NoofAttendees"]
    EventDate = request.POST["EventDate"]
    OwnerId = request.session.get('userid')
    eventinfo = EventInfo()
    eventinfo.EventName=EventName
    eventinfo.EventDescription=EventDescription
    eventinfo.EventLocation=EventLocation
    eventinfo.NoofAttendees=NoofAttendees
    eventinfo.EventDate=EventDate
    eventinfo.OwnerId = OwnerId
    print(request.session.get('userid'))
    eventinfo.save()
    print("after")
    events = EventInfo.objects.all()
    return render(request, 'Event_Dashbord.html', {'events' : events})

""" def created_event(request, id): 
    return render_to_response('Created_Event.html', {
        'event' : get_object_or_404(EventInfo, id=id)
    }) """

class Created_Event(View): 
    def get(self, request, id):
        OwnerId = request.session.get('userid')
        user =  ProfileInfo.objects.get(id=OwnerId)
        event = EventInfo.objects.get(id=id)
        events = {
            'EventName' : event.EventName,
            'EventDescription' : event.EventDescription,
            'EventLocation' : event.EventLocation,
            'NoofAttendees' : event.NoofAttendees,
            'EventDate' : event.EventDate,
            'OwnerName' : user.firstName
        }
        return render_to_response('Created_Event.html', {'event' : events})

class Join_Event(View): 
    def get(self, request, id): 
        return HttpResponse("Event Joined")

class Delete_Event(View):
    def get(self, request, id):
        b = EventInfo.objects.get(id=id)
        b.delete()
        events = EventInfo.objects.all()
        return render(request, 'Event_Dashbord.html', {'events' : events})

""" def delete_event(request, id):
    b = EventInfo.objects.get(id=id)
    b.delete()
    events = EventInfo.objects.all()
    return render(request, 'Event_Dashbord.html', {'events' : events}) """
class Event_Data_Fetch(View):
    def get(self, request, id):
        return render_to_response('Edit_Event.html', {
            'event' : get_object_or_404(EventInfo, id=id)
    })

""" def edit_event(request, id):
    return render_to_response('Edit_Event.html', {
        'event' : get_object_or_404(EventInfo, id=id)
    })
 """
def edit_event_post(request, id):
    print("hit")
    #EventName =  request.POST["EventName"]
    #slug = request.POST["slug"]
    #EventDescription =  request.POST["EventDescription"]
    #EventLocation =  request.POST["EventLocation"]
    #NoofAttendees =  request.POST["NoofAttendees"]
    #EventDate = request.POST["EventDate"]
    # event = get_object_or_404(EventInfo, id=id)
    # if request.method == "POST":
    #     form = PostForm(request.POST , instance=event)
    #     if form.is_valid():
    #         event = form.save(commit = false)
    #         event.EventName = request.EventName
    #         event.save()
    #         return render(request, 'Event_Dashbord.html', {'events' : events})
    EventName =  request.POST["EventName"]
    EventDescription =  request.POST["EventDescription"]
    EventLocation =  request.POST["EventLocation"]
    NoofAttendees =  request.POST["NoofAttendees"]
    EventDate = request.POST["EventDate"]
    eventinfo = EventInfo.objects.get(id=id)
    print("before update")
    eventinfo.EventName= EventName
    eventinfo.EventDescription= EventDescription
    eventinfo.EventLocation = EventLocation
    eventinfo.NoofAttendees = NoofAttendees
    eventinfo.EventDate = EventDate
    eventinfo.update()
    print("after update")
    events = EventInfo.objects.all()
    return render(request, 'Event_Dashbord.html', {'events' : events})