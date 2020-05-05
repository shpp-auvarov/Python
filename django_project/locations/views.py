from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import City, Country


# @login_required
# def index(request):
#     # return HttpResponse("Hello, world. You're at the locations index.")
#     countries = Country.objects.order_by('-name')[:5]
#     output = ', '.join([q.name for q in countries])
#     return HttpResponse(output)


@login_required
def text_return_only(request, text=""):
    return HttpResponse(text)


# def login(request):
#     context = {
#         'name': 'Login',
#     }
#     return render(request, 'locations/login.html', context)


@login_required
def get_countries(request):
    set_of_countries = Country.objects.order_by('name')
    print(set_of_countries)
    content = {
        'countries_list': set_of_countries,
    }
    return render(request, 'locations/countries.html', content, )


@login_required
def get_city(request, city_id):
    city_object = get_object_or_404(City, id=city_id)
    print(city_object)
    content = {
        'city': city_object,
    }
    return render(request, 'locations/city.html', content)


@login_required
def get_country(request, country_id):
    print("country_id = %s" % country_id)
    country = get_object_or_404(Country, id=country_id)
    cities = City.objects.filter(country=country_id).values()
    print(cities)
    content = {
        'country': country,
        'cities': cities,
    }
    return render(request, 'locations/country.html', content)


@login_required
def remove_city(request, country_id, city_id):
    try:
        City.objects.get(pk=city_id).delete()
        print('Successful removing %s' % city_id)
    except ObjectDoesNotExist:
        print('ObjectDoesNotExist %s' % city_id)
    except:
        print('Not found %s' % city_id)
    return redirect('locations:country', country_id)
