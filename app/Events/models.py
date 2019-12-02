from django.db import models
from django.urls import reverse

# Create your models here.

class EventInfo(models.Model):
    EventName = models.CharField(max_length = 200)
    slug = models.SlugField(max_length=255, unique=True)
    EventDescription = models.CharField(max_length = 200)
    EventLocation = models.CharField(max_length = 200)
    NoofAttendees = models.CharField(max_length = 100)
    EventDate = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.EventName
    
    def get_absolute_url(self):
        return reverse('Event.views.event_creation_post', args=[self.slug])