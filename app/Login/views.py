from django.shortcuts import render, HttpResponse
from Profile.models import ProfileInfo
from Events.models import EventInfo
#from social.apps.django_app.default.models import social_auth_usersocialauth


# Create your views here.
def login(request):
    return HttpResponse('login')
    
def index(request):
    return render(request, 'Login.html')


def login_post(request):
    InputEmail = request.POST["userEmail"]
    #userPassword = request.POST["userPassword"]
    try:
        ProfileInfo_ = ProfileInfo.objects.get(inputEmail=InputEmail) 
        events = EventInfo.objects.all()
        return render(request, 'Event_Dashbord.html', {'events' : events})
    except ProfileInfo.DoesNotExist: 
        print("username..")
        return render(request, 'Login.html')



