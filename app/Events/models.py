from django.db import models
from django.urls import reverse
from Profile.models import ProfileInfo



class EventInfo(models.Model):
    EventName = models.CharField(max_length = 200)
    EventDescription = models.CharField(max_length = 200)
    EventLocation = models.CharField(max_length = 100)
    NoofAttendees = models.CharField(max_length = 100)
    EventDate = models.DateTimeField(blank=True, null=True)
    OwnerId = models.PositiveSmallIntegerField(default=0,null=True)
    Attendee = models.ManyToManyField(ProfileInfo, blank= True)

def __str__(self):
    return self.EventName

    
    
   