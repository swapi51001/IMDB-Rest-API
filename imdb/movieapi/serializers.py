from pyexpat import model
from rest_framework import serializers
from .models import Moviesdata

class MoviesdataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moviesdata
        fields = '__all__'
