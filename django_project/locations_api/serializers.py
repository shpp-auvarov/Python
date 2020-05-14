from rest_framework import serializers

import locations.models


class SymbolSerializer(serializers.ModelSerializer):
    class Meta:
        model = locations.models.Symbol
        fields = ['pk', 'image']


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = locations.models.Country
        fields = ['pk', 'name', 'description', 'population', 'flag', 'cities_count']


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = locations.models.City
        fields = ['pk', 'name', 'country', 'longitude', 'latitude']
