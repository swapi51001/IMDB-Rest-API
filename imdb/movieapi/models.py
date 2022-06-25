
from django.db import models



class Moviesdata(models.Model):
    id = models.IntegerField(blank=True, null=False,primary_key=True)
    movie_title = models.CharField(max_length=100, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    place = models.IntegerField(blank=True, null=True)
    rating = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    link = models.CharField(max_length=100, blank=True, null=True)
    poster = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        ordering =['id']
        db_table = 'moviesdata'
