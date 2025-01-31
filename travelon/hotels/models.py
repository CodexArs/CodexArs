from django.db import models
from django import forms
from django.forms import DateTimeInput

# Create your models here.

class HotelPartnerList(models.Model):
    HOTELID =  models.AutoField(primary_key=True, editable=False, auto_created = True, serialize = False)
    HOTELNAME = models.TextField(max_length=100)
    LOCATION = models.TextField(max_length=250)
    CITY = models.TextField(max_length=100)
    CHECKIN = models.TextField(max_length=30)
    CHECKOUT = models.TextField(max_length=30)
    AMENITIES = models.TextField(max_length=100)
    IMAGE = models.ImageField(default="Image")

    class Meta:
        db_table = "hotelpartner"

    def __str__(self):
        return f"{self.HOTELID } | { self.HOTELNAME } | {self.LOCATION} | {self.CITY} | { self.CHECKIN } | {self.CHECKOUT} | {self.AMENITIES}"
    
class HotelCities(models.Model):
    CITYID = models.AutoField(primary_key=True, editable=False, auto_created=True, serialize=False)
    CITY = models.TextField(max_length=100)

    class Meta:
        db_table = "hotelcities"

    def __str__(self):
        return f"{self.CITYID } {self.CITY }"
    

class BootstrapDateTimePickerInput(DateTimeInput):
    template_name = 'widgets/bootstrap_datetimepicker.html'

    def get_context(self, name, value, attrs):
        datetimepicker_id = 'datetimepicker_{name}'.format(name=name)
        if attrs is None:
            attrs = dict()
        attrs['data-target'] = '#{id}'.format(id=datetimepicker_id)
        attrs['class'] = 'form-control datetimepicker-input'
        context = super().get_context(name, value, attrs)
        context['widget']['datetimepicker_id'] = datetimepicker_id
        return context