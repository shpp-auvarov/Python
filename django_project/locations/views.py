from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import City, Country


@login_required
def index(request):
    # return HttpResponse("Hello, world. You're at the locations index.")
    countries = Country.objects.order_by('-name')[:5]
    output = ', '.join([q.name for q in countries])
    return HttpResponse(output)


@login_required
def text_return_only(request, text=""):
    return HttpResponse(text)


def login(request):
    context = {
        'name': 'Login',
    }
    return render(request, 'locations/login.html', context)


@login_required
def list_of_countries(request):
    set_of_countries = Country.objects.order_by('name').values()
    entry_list = list(set_of_countries)
    print(entry_list)
    countries_list = []
    for item in entry_list:
        countries_list.append(item['name'])
    print(countries_list)
    content = {
        'countries_list': countries_list,
    }
    return render(request, 'locations/list_of_countries.html', content, )


@login_required
def city(request, name):
    city_object = get_object_or_404(City, name=name)
    print(city_object)
    print(city_object._meta.get_fields())
    country_object = get_object_or_404(Country, name=getattr(city_object, 'country'))
    country_name = getattr(country_object, 'name')
    content = {
        'initial_name': name,
        'id': getattr(city_object, 'id'),
        'name': getattr(city_object, 'name'),
        'country': getattr(city_object, 'country'),
        'country_name': country_name,
        'longitude': getattr(city_object, 'longitude'),
        'latitude': getattr(city_object, 'latitude'),
    }
    return render(request, 'locations/city.html', content)


@login_required
def country(request, name):
    print(name)
    country_object = get_object_or_404(Country, name=name)
    country_id = getattr(country_object, 'id')
    print(country_id)
    cities = City.objects.all().filter(country=country_id).values()
    print(cities)
    cities_list = []
    for item in cities:
        dict = {'id': item['id'], 'name': item['name'], 'country_id': item['country_id'],
                'longitude': item['longitude'], 'latitude': item['latitude']}
        cities_list.append(dict)
    print(cities_list)
    content = {
        'name': name,
        'country_id': country_id,
        'description': getattr(country_object, 'description'),
        'population': getattr(country_object, 'population'),
        'flag': getattr(country_object, 'flag'),
        'cities_count': getattr(country_object, 'cities_count'),
        'cities': cities_list,
    }
    return render(request, 'locations/country.html', content)


@login_required
def remove_city(request, name, city):
    try:
        City.objects.get(name=city).delete()
        print('Successful removing ' + city)
    except:
        print('Not found ' + city)

    return country(request, name)
