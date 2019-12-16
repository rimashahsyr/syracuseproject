from django import forms
from .models import ProfileInfo

#form for creating and editing a profile.
class ProfileForm(forms.ModelForm):
    
    class Meta:
        model= ProfileInfo
        fields = ('firstName', 'lastName', 'inputEmail', 'phoneNumber', 'dateOfBirth','locationCriteria', 'eventCategories')
        #fields = '_all_'