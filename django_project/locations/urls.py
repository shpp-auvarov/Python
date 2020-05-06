from django.urls import path

from . import views

app_name = 'locations'
urlpatterns = [
    path('', views.get_countries),
    # path('login', views.login, name='login'),
    path('countries', views.get_countries, name='countries'),
    # path('', views.get_countries, name='list_of_countries'),
    path('city/<int:city_id>', views.get_city, name='city'),
    path('country/<int:country_id>', views.get_country, name='country'),
    path('country/<int:country_id>/remove/<int:city_id>', views.remove_city, name='remove_city'),
    path('country/remove/<int:country_id>', views.remove_country, name='remove_country'),
    path('<str:text>', views.text_return_only),
    path('city/create', views.create_new_city, name='create_new_city'),
    path('city/edit/<int:city_id>', views.edit_city, name='edit_city'),
    path('country/create', views.create_new_country, name='create_new_country'),
    path('country/edit/<int:country_id>', views.edit_country, name='edit_country'),
]
