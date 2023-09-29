from django.db import models
from django_countries.fields import CountryField

CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
]

# Create your models here.
class UserProfile(models.Model):
    emplyoee_name = models.CharField(max_length=100)
    mobile_number = models.PositiveIntegerField()
    date_of_birth = models.DateTimeField()
    gender = models.CharField(max_length=10, choices=CHOICES)
    address = models.TextField(max_length=150)
    country = CountryField()

    # skills
    is_AWS = models.BooleanField(default=False)
    is_Full_Stack_Developer = models.BooleanField(default=False)
    is_DevOps = models.BooleanField(default=False)

    def __str__(self):
        return self.emplyoee_name