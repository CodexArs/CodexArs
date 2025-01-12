from django.shortcuts import render

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






