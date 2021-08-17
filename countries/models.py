from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=200)
    alpha2Code = models.CharField(max_length=10)
    capital = models.CharField(max_length=200)
    population = models.CharField(max_length=200, blank=True)
    timezone = models.CharField(max_length=200, blank=True)
    flag = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=200)
    countries = models.ManyToManyField(Country, related_name="languages")

    def __str__(self):
        return self.name

class Neighbour(models.Model):
    name = models.CharField(max_length=200)
    alpha3Code = models.CharField(max_length=10)
    countries = models.ManyToManyField(Country, related_name="neighbours")

    def __str__(self):
        return self.name