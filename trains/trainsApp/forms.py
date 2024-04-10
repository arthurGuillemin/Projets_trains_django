from django import forms
from .models import Trains

class TrainsForm(forms.ModelForm):
    class Meta:
        model = Trains
        fields = ['origine', 'destination', 'heure_de_depart', 'heure_arrive', 'description']
