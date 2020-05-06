from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver


# Create your models here.


class Symbol(models.Model):
    class Meta:
        verbose_name = "Symbol"
        verbose_name_plural = "Symbols"

    image = models.ImageField(unique=True, null=False, blank=False)

    def __str__(self):
        try:
            return self.symbol.name + " symbol"
        except Exception:
            return 'Symbol'


class Country(models.Model):
    class Meta:
        verbose_name_plural = "Countries"

    name = models.CharField(null=False, blank=False, max_length=100)
    description = models.TextField(null=True)
    population = models.IntegerField(default=0)
    flag = models.OneToOneField(Symbol, on_delete=models.CASCADE, related_name='symbol')
    cities_count = models.IntegerField(default=0)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class City(models.Model):
    class Meta:
        verbose_name_plural = "Cities"

    name = models.CharField(null=False, blank=False, max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='country')
    longitude = models.FloatField(null=False)
    latitude = models.FloatField(null=False)

    def __str__(self):
        return self.name


@receiver(pre_save, sender=City)
def pre_save_handler(sender, instance, **kwargs):
    print("City " + instance.name + " will be added")


@receiver(post_save, sender=City)
def post_save_handler(sender, instance, **kwargs):
    print("instance.country.cities_count = %s" % instance.country.cities_count)
    instance.country.cities_count = City.objects.filter(country=instance.country).count()
    # instance.country.cities_count += 1
    instance.country.save()


@receiver(pre_delete, sender=City)
def pre_delete_handler(sender, instance, **kwargs):
    print("instance.country.cities_count = %s" % instance.country.cities_count)
    instance.country.cities_count -= 1
    instance.country.save()


@receiver(post_delete, sender=City)
def post_delete_handler(sender, instance, **kwargs):
    print("City " + instance.name + " removed")
