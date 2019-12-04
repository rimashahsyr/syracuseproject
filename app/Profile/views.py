from django.shortcuts import render, render_to_response, get_object_or_404
from .models import ProfileInfo

# Create your views here.
def profile_creation(request):
    return render(request, 'Profile_creation.html')



def profile_creation_post(request):
    firstName = request.POST["firstName"]
    lastName = request.POST["lastName"]
    inputEmail = request.POST["inputEmail"]
    userPassword = request.POST["userPassword"]
    phoneNumber = request.POST["phoneNumber"]
    dateOfBirth = request.POST["dateOfBirth"]
    locationCriteria = request.POST.getlist("locationCriteria")
    eventCategories = request.POST.getlist("eventCategories")

    profileInfo = ProfileInfo()
    profileInfo.firstName=firstName
    profileInfo.lastName=lastName
    profileInfo.inputEmail=inputEmail
    profileInfo.userPassword=userPassword
    profileInfo.phoneNumber=phoneNumber 
    profileInfo.dateOfBirth=dateOfBirth
    profileInfo.locationCriteria=locationCriteria
    profileInfo.eventCategories=eventCategories
    profileInfo.save()
    return created_profile(request, inputEmail)

def created_profile(request, inputEmail): 
    return render_to_response('Created_Profile.html', {
        'profile' : get_object_or_404(ProfileInfo, inputEmail=inputEmail)
    })