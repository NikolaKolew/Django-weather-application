from django import forms

from weather_application.webapp.models import City


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'
