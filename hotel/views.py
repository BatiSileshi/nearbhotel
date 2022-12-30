from django.shortcuts import render

# from django.views import generic
from django.contrib.gis.geos import  Point
from django.contrib.gis.db.models.functions import Distance
from .models import Hotel
# import requests
# import json



    
def home(request):
     
    hotels = Hotel.objects.all()
    
    longitude = 36.81563
    latitude = 7.69745


    user_location = Point(longitude, latitude, srid=4326)
    
    hotels = Hotel.objects.annotate(distance=Distance('location', user_location)).order_by('distance')

    
    context={'hotels':hotels, 'user_location':user_location}
    return render(request, 'hotel/index.html', context)
# 7.68724
# 36.86988