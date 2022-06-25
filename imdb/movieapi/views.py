from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.parsers import JSONParser
from rest_framework.filters import SearchFilter,OrderingFilter
from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


from . import models
from . import serializers

from movieapi.models import Moviesdata
from movieapi.serializers import MoviesdataSerializer


#def movieApi(request):
#    if request.method =='GET':
#        movies = Moviesdata.objects.all()
#        movies_serializer = MoviesdataSerializer(movies,many=True)
#        return JsonResponse(movies_serializer.data, safe=False)

class MovieList(ListAPIView):
    queryset = models.Moviesdata.objects.all()
    serializer_class = serializers.MoviesdataSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['movie_title']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    