from django.db import models

### ADD ###
from datetime import datetime

# Create your models here.
class Booking(models.Model):
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField(max_length=6)
    BookingDate = models.DateField(default=datetime.now())

    def __str__(self):
        return self.Name


# Add code to create Menu model
class Menu(models.Model):
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.IntegerField(max_length=5)

    def __str__(self):
        return f"{self.title} : {str(self.price)}"


class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()

    def get_item(self):
        return f"{self.title} : {str(self.price)}"
