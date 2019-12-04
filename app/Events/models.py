from django.db import models
from django.urls import reverse
from multiselectfield import MultiSelectField

# Create your models here.
location_choices = (('cafe_1', 'Starbucks'),
              ('cafe_2 ', 'Dunkin Donuts'),
              ('cafe_3', 'Recess'),
              ('cafe_4', 'Alto Chinco'),
              ('cafe_5', 'Gangnam Style'))

class EventInfo(models.Model):
    EventName = models.CharField(max_length = 200)
    EventDescription = models.CharField(max_length = 200)
    EventLocation = models.CharField(max_length = 200)
    NoofAttendees = models.CharField(max_length = 100)
    EventDate = models.DateTimeField(blank=True, null=True)

def __str__(self):
    return self.EventName

    
    
   