from django import forms

from weather_application.webapp.models import City


class AddCity(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'

class DeleteCity(forms.ModelForm):
    class Meta:
        model = City
        fields = ()

