from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible  # only if you need to support Python 2
class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, null=True, blank=True)
    lat = models.CharField(max_length=20, null=True, blank=True)
    lng = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=5)
    category = models.CharField(max_length=50, null=True, blank=True)
    image = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.name

class Diet(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Dish(models.Model):
    restaurant = models.ManyToManyField(Restaurant)
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=300, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    diet = models.ManyToManyField(Diet)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class User(models.Model):
    login = models.CharField(max_length=50)
    favourite_diet = models.ForeignKey(Diet, on_delete=models.CASCADE)

    def __str__(self):
        return self.login