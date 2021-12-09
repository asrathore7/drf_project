from rest_framework import serializers
from .models import Application
from django_countries.serializer_fields import CountryField

class ApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application
        fields = '__all__'

    def validate_name(self, value):
        if len(value) > 10:
            raise serializers.ValidationError(
                "Length of name should be less then 10..")
        return value
