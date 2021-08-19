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
    languages = LanguageSerializer(read_only=False, many=True, required=False)
    neighbours = NeighbourSerializer(
        read_only=False, many=True, required=False)

    class Meta:
        model = Country
        fields = "__all__"


class NeighbourIdSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=200)
    alpha3code = serializers.CharField(max_length=10)

    def validate_id(self, id):
        try:
            neighbour = Neighbour.objects.get(pk=id)
        except Neighbour.DoesNotExist:
            raise serializers.ValidationError('Neighbour does not exist')
        return neighbour


class CountryWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"
