from django.shortcuts import render

# from .models import HotelPartner

# Create your views here.

def navbar(request):
    return render(request, 'navbar/nav.html')  


# def hotelpartner(request):
#     if request.method == "POST":
#         searchhotel = request.POST ['searchhotel']
#         hotels  = HotelPartner.objects.filter(HOTELNAME__icontains=searchhotel ) | HotelPartner.objects.filter(LOCATION__icontains=searchhotel )
#         return render(request, 'navbar/search-hotels.html', { 'searchhotel':searchhotel, 'hotels':hotels })
#     else :
#         return render(request, 'navbar/search-hotels.html', { } )






