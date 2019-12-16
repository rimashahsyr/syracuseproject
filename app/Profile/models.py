from django.db import models

# Create your models here.

#Model for Profile Infromation Class
class ProfileInfo(models.Model):
    firstName = models.CharField(max_length=250)
    lastName = models.CharField(max_length=250)
    inputEmail = models.CharField(max_length=250)
    userPassword = models.CharField(max_length=250)
    phoneNumber = models.BigIntegerField()
    dateOfBirth = models.DateTimeField(blank=True, null=True)
    locationCriteria = models.CharField(max_length=250)
    eventCategories = models.CharField(max_length=250)

    # Constructor for the class to return the firstname when the class is invoked.
    def __str__(self):
            return self.firstName