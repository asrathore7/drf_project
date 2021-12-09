from django.db import models
from django_countries.fields import CountryField
from django.conf import settings

class Application(models.Model):
    application_type = (
        ('c1', 'C1'),
        ('c2', 'C2'),
        ('c3', 'C3')
    )

    name = models.CharField(max_length=20)
    street = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=30, blank=True)
    zip_code = models.CharField(max_length=6, default="452001")
    type =  models.CharField(max_length=20, choices=application_type, default='c1')
    country = CountryField(max_length=30, blank=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return  '{} > {}'.format(self.name, self.type)
