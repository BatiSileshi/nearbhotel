from django.shortcuts import render

from django.views import generic
from django.contrib.gis.geos import fromstr, Point
from django.contrib.gis.db.models.functions import Distance
from .models import Hotel
import requests
import json


# api_key = '3c22e730d3cb43f5bc6d9d492f80f9f8'

# api_url = 'https://ipgeolocation.abstractapi.com/v1/?api_key=3c22e730d3cb43f5bc6d9d492f80f9f8' + api_key

# def get_ip_geolocation_data(ip_address):
#     response = requests.get("https://ipgeolocation.abstractapi.com/v1/?api_key=3c22e730d3cb43f5bc6d9d492f80f9f8")
#     print(ip_address)
#     # print(response.content)
#     response = requests.get(api_url)

#     return response.content


# longitude = 9.5704819
# latitude = 41.0631088,6


# user_location = Point(longitude, latitude, srid=4326)

# class Home(generic.ListView):
#     model = Hotel
#     context_object_name = 'hotels'
#     queryset = Hotel.objects.annotate(distance=Distance('location',
#     user_location)
#     ).order_by('distance')[0:6]
#     template_name = 'hotel/index.html'
    
def home(request):
     
    hotels = Hotel.objects.all()
    
    longitude = 36.81563
    latitude = 7.69745


    user_location = Point(longitude, latitude, srid=4326)
    
    hotels = Hotel.objects.annotate(distance=Distance('location', user_location))

    
    context={'hotels':hotels, 'user_location':user_location}
    return render(request, 'hotel/index.html', context)
# 7.68724
# 36.86988