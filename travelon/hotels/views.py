from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
from django.core import serializers
from django.template import loader

# Create your views here.

from .models import HotelPartnerList, HotelCities

# home page of hotel booking 
def home(request):
    hotelsuggestion = HotelPartnerList.objects.all()  
    return render(request, 'hotels/home.html' )  
    
# def hotelpartner(request):
#     if request.method == "POST":
#         searchhotel = request.POST ['searchhotel']
#         hotels  = HotelPartnerList.objects.filter(HOTELNAME__icontains=searchhotel ) | HotelPartnerList.objects.filter(LOCATION__icontains=searchhotel )
#         return render(request, 'navbar/search-hotels.html', { 'searchhotel':searchhotel, 'hotels':hotels })
#     else :
#         return render(request, 'navbar/search-hotels.html', { } )
    
def view_hotels(request):
    data = serializers.serialize('json', HotelPartnerList.objects.all())
    return HttpResponse(data, content_type='application/json')
    
# search hotels based on the locations 
def searchhotel(request):
    name = request.GET.get('name')
    hotellist = []
    if name:
        hotels =  HotelCities.objects.filter(CITY__icontains=name)
        for hotel in hotels:
            hotellist.append((hotel.CITY))
    return JsonResponse({'status':200, 'data': hotellist})


# get the list of hotels in the locations 
def hotel_location(request,name):
    hotels =  HotelPartnerList.objects.filter(CITY__icontains=name)
    name = []
    for hotel in hotels:
        name.append({ 'name' : hotel.HOTELNAME,
                      'location': hotel.LOCATION
                    })
    if not hotels:
        template = loader.get_template('hotels/error.html')
    else:
        template = loader.get_template('hotels/hotel-location.html')
    context = { 
        'name' : name 
    }
    return HttpResponse(template.render(context, request))



