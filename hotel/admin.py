from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Hotel

@admin.register(Hotel)
class ShopAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')
    
