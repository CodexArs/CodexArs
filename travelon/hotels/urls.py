from django.urls import path

# from .views import  index
from . import views

app_name="hotels"

urlpatterns = [
    path("", views.home, name="hotels"),
    # path("search-hotels/", views.hotelpartner, name="search-hotels")
    path("search-hotels/", views.searchhotel, name="search-hotels"),
    path("view-hotels/", views.view_hotels, name="view-hotels"), 
    path("list/<str:name>", views.hotel_location, name="hotel-list-location")
   
]


