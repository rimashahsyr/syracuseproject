from django.shortcuts import render
from .models import ProfileInfo

# Create your views here.
def profile_creation(request):
    return render(request, 'Profile_creation.html')


def profile_creation_post(request):
    firstName = request.POST["firstName"]
    lastName = request.POST["lastName"]
    inputEmail = request.POST["inputEmail"]
    phoneNumber = request.POST["phoneNumber"]
    dateOfBirth = request.POST["dateOfBirth"]
    locationCriteria = request.POST["locationCriteria"]
    eventCategories = request.POST["eventCategories"]

    profileInfo = ProfileInfo()
    profileInfo.firstName=firstName
    profileInfo.lastName=lastName
    profileInfo.inputEmail=inputEmail
    profileInfo.phoneNumber=phoneNumber 
    profileInfo.dateOfBirth=dateOfBirth
    profileInfo.locationCriteria=locationCriteria
    profileInfo.eventCategories=eventCategories
    print("before Saving")
    profileInfo.save()
    print("After Saving")
    return render(request, "Profile_creation.html")
