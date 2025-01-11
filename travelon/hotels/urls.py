from django.urls import path

# from .views import  index
from . import views

app_name="hotels"

urlpatterns = [
    path("", views.home, name="hotels"),
   
]


