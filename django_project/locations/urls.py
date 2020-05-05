from django.urls import path

from . import views

app_name = 'locations'
urlpatterns = [
    # path('', views.index),
    # path('login', views.login, name='login'),
    path('countries', views.get_countries, name='countries'),
    # path('', views.get_countries, name='list_of_countries'),
    path('city/<int:city_id>', views.get_city, name='city'),
    path('country/<int:country_id>', views.get_country, name='country'),
    path('country/<int:country_id>/remove/<int:city_id>', views.remove_city, name='remove_city'),
    path('<str:text>', views.text_return_only),
]
