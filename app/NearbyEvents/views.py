from django.shortcuts import render
from mapbox import Directions
from .models import LocationPreferences
from django.core.serializers import serialize
# Create your views here.
# TODO: move Token to settings.py file

def default_maps(request):
    locationPreferences = LocationPreferences()
    """ lat = locationPreferences.lat
    lon = locationPreferences.lon """
    #locations = LocationPreferences.objects.all()
    locations = serialize('json', LocationPreferences.objects.all())
    #print (locations.cafeName)


    
    mapbox_access_token = 'pk.eyJ1IjoicmltYXNoYWg5NTk1IiwiYSI6ImNrNDg2ODZldjEyZzYzZW5uc3R2amthdzkifQ.nO-Z3ySyMnhhTlEeuBxYag'
	
    return render(request, 'NearbyEvents.html', {'mapbox_access_token':mapbox_access_token, 'locations' : locations })