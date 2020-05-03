from django.urls import path

from . import views

app_name = 'locations'
urlpatterns = [
    path('', views.index),
    path('login', views.login, name='login'),
    path('list_of_countries', views.list_of_countries, name='list_of_countries'),
    path('city/<str:name>', views.city, name='city'),
    path('country/<str:name>', views.country, name='country'),
    path('country/<str:name>/remove_city/<str:city>', views.remove_city, name='country'),
    path('<str:text>', views.index_second),
]
