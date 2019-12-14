from django.shortcuts import render, HttpResponse, render_to_response
from Profile.models import ProfileInfo
from Events.models import EventInfo
from django.contrib import messages
from django.template import RequestContext
#from social.apps.django_app.default.models import social_auth_usersocialauth


# Create your views here.
def login(request):
    return HttpResponse('login')
    
def index(request):
    return render(request, 'Login.html')


def login_post(request):
    InputEmail = request.POST["userEmail"]
    userPassword = request.POST["userPassword"]

    try:
        ProfileInfo_ = ProfileInfo.objects.get(inputEmail=InputEmail, userPassword=userPassword)
        events = EventInfo.objects.all() 
		#return render(request, 'Event_Dashbord.html', {'events' : events})
        messages.success(request, 'SUCCESS!')
        session_id = request.session.get('userid',0) 
        request.session['userid'] = ProfileInfo_.id
        id_session = request.session.get('userid')
        id = request.session['id']
        # context = {
        #     'EventName' : events.EventName,
        #     'EventDescription' : events.EventDescription,
        #     'EventLocation' : events.EventLocation,
        #     'NoofAttendees' : events.NoofAttendees,
        #     'EventDate' : events.EventDate,
        #     'Userid' : request.session.get('id', 0)
        # }
        return render(request, 'Event_Dashbord.html', {'events' : events ,'id': id_session})
        #return render_to_response('Event_Dashbord.html', 
        #{'events' : events}, context_instance=RequestContext(request))
    
    except ProfileInfo.DoesNotExist: 
        print("username..")
        messages.error(request, "Username or Password not correct.")
        return render(request, 'Login.html')



