from django import forms

from .models import Country, City


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ('__all__')


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ('__all__')
