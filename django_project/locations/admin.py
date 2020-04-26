from django.contrib import admin

# Register your models here.
from .models import Symbol, Country, City

admin.site.register(Symbol)


# admin.site.register(Country)
# admin.site.register(City)


# Define the admin class
class CountryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'description', 'population', 'flag', 'cities_count')


# Register the admin class with the associated model
admin.site.register(Country, CountryAdmin)


# Define the admin class
class CityAdmin(admin.ModelAdmin):
    list_filter = ('country',)
    list_display = ('name', 'country', 'longitude', 'latitude')


# Register the admin class with the associated model
admin.site.register(City, CityAdmin)
