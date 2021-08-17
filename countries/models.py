from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Neighbour(models.Model):
    name = models.CharField(max_length=200)
    alpha3Code = models.CharField(max_length=10)

    def __str__(self):
        return self.name
class Country(models.Model):
    name = models.CharField(max_length=200)
    alpha2Code = models.CharField(max_length=10)
    capital = models.CharField(max_length=200)
    population = models.CharField(max_length=200, blank=True)
    timezone = models.CharField(max_length=200, blank=True)
    flag = models.TextField(blank=True)
    languages = models.ManyToManyField(Language, related_name="countries")
    neighbours = models.ManyToManyField(Neighbour, related_name="countries")

    def __str__(self):
        return self.name

