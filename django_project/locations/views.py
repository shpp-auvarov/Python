from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .forms import CountryForm, CityForm
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


@login_required
def remove_country(request, country_id):
    try:
        Country.objects.get(pk=country_id).delete()
        print('Successful removing %s' % country_id)
    except ObjectDoesNotExist:
        print('ObjectDoesNotExist %s' % country_id)
    except:
        print('Not found %s' % country_id)
    return redirect('locations:countries')


@login_required
def create_new_country(request):
    if request.method == "POST":
        form = CountryForm(request.POST)
        print('Form here - create_new_country')
        if form.is_valid():
            print('Valid')
            country = form.save(commit=False)
            country.save()
            return redirect('locations:country', country.id)
        else:
            print('Not valid')
    else:
        print('Method not post')
        form = CountryForm()
    return render(request, 'locations/country_create_new.html', {'form': form})


@login_required
def edit_country(request, country_id):
    country = get_object_or_404(Country, id=country_id)
    if request.method == "POST":
        form = CountryForm(request.POST, instance=country)
        print('Form here')
        if form.is_valid():
            print('Valid')
            country = form.save(commit=False)
            country.save()
            return redirect('locations:country', country_id)
        else:
            print('Not valid')
    else:
        print('Method not post')
        form = CountryForm(instance=country)
    return render(request, 'locations/country_edit.html', {'form': form})


@login_required
def create_new_city(request):
    if request.method == "POST":
        form = CityForm(request.POST)
        print('Form here - create_new_city')
        if form.is_valid():
            print('Valid')
            city = form.save(commit=False)
            city.save()
            return redirect('locations:city', city.id)
        else:
            print('Not valid')
    else:
        print('Method not post')
        form = CityForm()
    return render(request, 'locations/city_create_new.html', {'form': form})


@login_required
def edit_city(request, city_id):
    city = get_object_or_404(City, id=city_id)
    if request.method == "POST":
        form = CityForm(request.POST, instance=city)
        print('Form here')
        if form.is_valid():
            print('Valid')
            city = form.save(commit=False)
            city.save()
            return redirect('locations:city', city_id)
        else:
            print('Not valid')
    else:
        print('Method not post')
        form = CityForm(instance=city)
    return render(request, 'locations/city_edit.html', {'form': form})
