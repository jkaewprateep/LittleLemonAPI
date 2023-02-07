from rest_framework import serializers
from .models import Booking, Menu, MenuItem

### ADD ###
from django.contrib.auth.models import User


class BookingSerializer(serializers.Serializer):
    class Meta:
        model = Booking
        fields = "__all__"


class MenuSerializer(serializers.Serializer):
    class Meta:
        model = Menu
        fields = "__all__"


# define Serializer class for User model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ["id", "title", "price", "inventory"]
