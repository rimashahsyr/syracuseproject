from django.db import models

# Create your models here.

class EventInfo(models.Model):
    EventName = models.CharField(max_length = 200)
    EventDescription = models.CharField(max_length = 200)
    EventLocation = models.CharField(max_length = 200)
    NoofAttendees = models.CharField(max_length = 100)
    EventDate = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.EventName
