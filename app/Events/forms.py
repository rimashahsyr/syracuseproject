from django import forms
from .models import EventInfo

class EventForm(forms.ModelForm):
    
    class Meta:
        model= EventInfo
        fields = ('EventName', 'EventDescription', 'EventLocation', 'NoofAttendees', 'EventDate')
        #fields = '__all__'
        widgets = {
            'EventDate': forms.DateTimeInput(attrs={'class':'form-control'}),
        }

