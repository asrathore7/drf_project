from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django_countries.fields import CountryField

class User(AbstractUser):
    street = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=30, blank=True)
    country = CountryField(max_length=30, blank=True)
