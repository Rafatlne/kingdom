import django_filters
from .models import *


class LanguageFilterSet(django_filters.FilterSet):
    language = django_filters.CharFilter(field_name='languages__name')

    class Meta:
        model = Country
        fields = ['language']
