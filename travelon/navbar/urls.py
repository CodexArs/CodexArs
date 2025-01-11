from django.urls import path

# from .views import  index
from . import views

app_name="navbar"

urlpatterns = [
    path("", views.navbar, name="navbar"),
   
]


