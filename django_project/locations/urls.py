from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('<str:text>/', views.index_second),
]
