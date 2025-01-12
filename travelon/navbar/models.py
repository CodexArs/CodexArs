from django.db import models

# Create your models here.

class HotelPartner(models.Model):
    HOTELID =  models.AutoField(primary_key=True, editable=False, auto_created = True, serialize = False)
    HOTELNAME = models.TextField(max_length=100)
    LOCATION = models.TextField(max_length=250)
    CHECKIN = models.TextField(max_length=30)
    CHECKOUT = models.TextField(max_length=30)
    AMENITIES = models.TextField(max_length=100)

    class Meta:
        db_table = "hotelpartner"

    def __str__(self):
        return f"| {self.HOTELID } | { self.HOTELNAME } | {self.LOCATION} | { self.CHECKIN } | {self.CHECKOUT} | {self.AMENITIES}"
    
    