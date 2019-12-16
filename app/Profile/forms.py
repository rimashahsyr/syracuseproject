from django import forms
from .models import ProfileInfo

class ProfileForm(forms.ModelForm):
    
    class Meta:
        model= ProfileInfo
        fields = ('firstName', 'lastName', 'inputEmail', 'phoneNumber', 'dateOfBirth','locationCriteria', 'eventCategories')
        #fields = '_all_'