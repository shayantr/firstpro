from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django import forms

from .models import *


class FlightForm(ModelForm):
    class Meta:
        model = Flight
        fields = '__all__'

    def clean(self):
        a = self.cleaned_data['origin']
        b = self.cleaned_data['destination']
        c = self.cleaned_date['duration']
        if a == b:
            raise ValidationError("origin and destination cannot be the same!")
        if Flight.objects.filter(origin=a) and Flight.objects.filter(destination=b):
            raise ValidationError("the flight already exists!")

class PassengerForm(ModelForm):
    class Meta:
        model = Passenger
        fields = '__all__'
