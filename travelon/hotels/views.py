from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
from django.core import serializers
from django.template import loader

# Create your views here.

from .models import HotelPartnerList

def home(request):
    # return render(request, 'navbar/nav.html')
    hotelsuggestion = HotelPartnerList.objects.all()  
    return render(request, 'hotels/home.html' , { 'hotelsuggestion':hotelsuggestion })  
    
def hotelpartner(request):
    if request.method == "POST":
        searchhotel = request.POST ['searchhotel']
        hotels  = HotelPartnerList.objects.filter(HOTELNAME__icontains=searchhotel ) | HotelPartnerList.objects.filter(LOCATION__icontains=searchhotel )
        return render(request, 'navbar/search-hotels.html', { 'searchhotel':searchhotel, 'hotels':hotels })
    else :
        return render(request, 'navbar/search-hotels.html', { } )
    
def view_hotels(request):
    data = serializers.serialize('json', HotelPartnerList.objects.all())
    return HttpResponse(data, content_type='application/json')
    

def searchhotel(request):
    name = request.GET.get('name')
    hotellist = []
    if name:
        hotels =  HotelPartnerList.objects.filter(LOCATION__icontains=name)
        for hotel in hotels:
            hotellist.append((hotel.LOCATION))
    return JsonResponse({'status':200, 'data': hotellist})

def search(request):
    return render(request, 'hotels/search-hotel.html')

def hotel_location(request,name):
    hotels =  HotelPartnerList.objects.filter(LOCATION__icontains=name)
    if not hotels:
        template = loader.get_template('hotels/error.html')
    else:
        template = loader.get_template('hotels/hotel-location.html')
    context = {
        'hotel': hotels,
    }
    return HttpResponse(template.render(context, request))



