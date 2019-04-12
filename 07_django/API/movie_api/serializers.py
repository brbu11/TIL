from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
