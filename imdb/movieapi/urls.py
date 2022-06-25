from django.conf.urls import url
from django.urls import path,include
from movieapi import views

urlpatterns =[
    path(r'movieapi$', views.MovieList)
]