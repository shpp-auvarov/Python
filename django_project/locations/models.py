from django.db import models


# Create your models here.

class Symbol(models.Model):
    image = models.ImageField(null=False, blank=False)


class Country(models.Model):
    name = models.CharField(null=False, blank=False, max_length=100)
    description = models.TextField(null=True)
    population = models.IntegerField(default=0)
    flag = models.OneToOneField(Symbol, on_delete=models.CASCADE)
    cities_count = models.IntegerField(default=0)
    users = models.ManyToManyField


class City(models.Model):
    name = models.CharField(null=False, blank=False, max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    longitude = models.FloatField(null=False)
    latitude = models.FloatField(null=False)


# Добавить в модель Country поле users со связью ManyToMany к стандартной модели пользователя. Создать миграции и провести их в базу.