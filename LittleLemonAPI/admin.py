from django.contrib import admin

### ADD ###
from .models import Menu, Booking

# Register your models here.
admin.site.register(Menu)
admin.site.register(Booking)
