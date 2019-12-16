from django import forms
from .models import EventInfo

class EventForm(forms.ModelForm):
    EventDate = forms.DateTimeField(
        label='Event Date',
        widget=forms.widgets.DateInput(attrs={'type':'date'}),
    )
    
    class Meta:
        model= EventInfo
        fields = ('EventName', 'EventDescription', 'EventLocation', 'NoofAttendees', 'EventDate')
        #fields = '__all__'
        widgets = {
            'EventDate': forms.DateTimeInput(attrs={'class':'form-control'}),
        }

