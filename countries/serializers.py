from rest_framework import serializers
from .models import *

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = "__all__"

class NeighbourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Neighbour
        fields = "__all__"

class CountrySerializer(serializers.ModelSerializer):
    languages = LanguageSerializer(read_only=True, many=True)
    neighbours = NeighbourSerializer(read_only=True, many=True)

    class Meta:
        model = Country
        fields = "__all__"