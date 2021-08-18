from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import viewsets
from .filters import *
from django.views import generic

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all().order_by('name')
    serializer_class = CountrySerializer

    filter_class = LanguageFilterSet
    search_fields = ['name']

    def get_serializer_class(self):

        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update':
            return CountryWriteSerializer

        return CountrySerializer
    
    @action(detail=True, methods=['GET'])
    def neighbours(self, request, pk=None):
        serializer = NeighbourIdSerializer(Country.objects.get(pk=pk).neighbours, many=True)
        return Response(serializer.data)

class CountryView(generic.TemplateView):
    template_name = 'countries/countries.html'
