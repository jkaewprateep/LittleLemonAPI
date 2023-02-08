from django.shortcuts import render

### ADD ###
from .models import Booking, Menu;
from .serializers import (
    BookingSerializer,
    MenuSerializer,
    UserSerializer
)
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
    ListAPIView,
    
)

# from .models import MenuItem
# from .serializers import MenuItemSerializer
from rest_framework.decorators import api_view

from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

### Project assignment ###
## Question 1 ##    Does the web application use Django to serve static HTML content?
import json;
from datetime import datetime;
from django.http import HttpResponse;
from django.views.decorators.csrf import csrf_exempt;
from django.core import serializers;


# from rest_framework.response import Response


# Create your views here.
# @api_view()
class BookingView(ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    ordering_fields = [ "Title", "Price", "Inventory" ];
    filterset_fields = [ "Title", "Price", "Inventory" ];
    search_fields = [ "Title", "Price", "Inventory" ];

    permission_classes = [IsAuthenticated]


# @api_view()
class MenuView(ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    ordering_fields = [ "Title", "Price", "Inventory" ];
    filterset_fields = [ "Title", "Price", "Inventory" ];
    search_fields = [ "Title", "Price", "Inventory" ];
    
# @api_view()
# class MenuItemView(ListCreateAPIView):
# class MenuItemView(ListCreateAPIView):
#     queryset = Menu.objects.all()
#     serializer_class = MenuSerializer
#     ordering_fields =[ "Title", "Price", "Inventory" ];
#     filterset_fields = [ "Title", "Price", "Inventory" ];
#     search_fields = [ "Title", "Price", "Inventory" ];


# @api_view()
class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    ordering_fields = [ "Title", "Price", "Inventory" ];
    filterset_fields = [ "Title", "Price", "Inventory" ];
    search_fields = [ "Title", "Price", "Inventory" ];


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    filterset_fileds = "__all__"


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = IsAuthenticated


@csrf_exempt
@api_view(['POST', 'PUT', 'DELETE'])
def MenuItemsView(request):
    
    if(request.method=='GET'):
        return []

    else:
       IsAuthenticated()
       
    if request.method == 'POST':
        # data = json.load(request)
        data = dict(request.data);
        exist = Menu.objects.filter(Title=data['Title']).exists()
        if exist==False:
            Menues = Menu(
                Title = data['Title'],
                Price = data['Price'],
                Inventory = data['Inventory'],
            )
            Menues.save()
        else:
            return HttpResponse("{'error':1}", content_type='application/json')

    elif request.method == 'PUT':
        data = dict(request.data);
        Title = data['Title']
        exist = Menu.objects.filter(Title=data['Title']).exists()
        if exist==False:
            Menues = Menu(
                Title = data['Title'],
                Price = data['Price'],
                Inventory = data['Inventory'],
            )
            Menues.save()
        else:
            
            menuId = Menu.objects.filter(Title=Title).values_list();
            menuId.update(
                Title = data['Title'],
                Price = data['Price'],
                Inventory = data['Inventory'],
            )

    elif request.method == 'DELETE':
        data = dict(request.data);
        Title = data['Title']
        exist = Menu.objects.filter(Title=data['Title']).exists()
        if exist==False:
            pass
        else:
            Menu.objects.filter(Title=Title).delete();
            
    menues = Menu.objects.all();
    menues_json = serializers.serialize('json', menues)

    return HttpResponse(menues_json, content_type='application/json')

@csrf_exempt
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def bookings(request):
    
    if(request.method=='GET'):
        return []

    else:
       IsAuthenticated()
    
    if request.method == 'POST':
        data = dict(request.data);
        exist = Booking.objects.filter(BookingDate=data['BookingDate'], Name=data['Name']).exists()
        if exist==False:
            booking = Booking(
                Name = data['Name'],
                No_of_guests = data['No_of_guests'],
                BookingDate = data['BookingDate'],
            )
            booking.save()
        else:
            return HttpResponse("{'error':1}", content_type='application/json')
        
        
    ###
    elif request.method == 'PUT':
        data = dict(request.data);
        exist = Booking.objects.filter(BookingDate=data['BookingDate'], Name=data['Name']).exists()
        if exist==False:
            Bookings = Booking(
                Name = data['Name'],
                No_of_guests = data['No_of_guests'],
                BookingDate = data['BookingDate'],
            )
            Bookings.save()
        else:
            
            BookingId = Booking.objects.filter(BookingDate=data['BookingDate'], Name=data['Name']).values_list();
            BookingId.update(
                Name = data['Name'],
                No_of_guests = data['No_of_guests'],
                BookingDate = data['BookingDate'],
            )

    elif request.method == 'DELETE':
        data = dict(request.data);
        exist = Booking.objects.filter(BookingDate=data['BookingDate'], Name=data['Name']).exists()
        if exist==False:
            pass
        else:
            Booking.objects.filter(BookingDate=data['BookingDate'], Name=data['Name']).delete();
    ###
    
    date = request.GET.get('date', datetime.today().date())

    # bookings = Booking.objects.all().filter(BookingDate=date)
    bookings = Booking.objects.all();
    booking_json = serializers.serialize('json', bookings)

    return HttpResponse(booking_json, content_type='application/json')


# Create your views here.
def index(request):
    return render(request, 'index.html', {})



## Create your views here.
# class MenuItemsView(generics.ListCreateAPIView):
#     queryset = MenuItem.objects.all();
#     serializer_class = MenuItemSerializer;

# class SingleMenuItemView(DestroyAPIView):
#     queryset = Menu.objects.all();
#     serializer_class = MenuSerializers;
#     ordering_fields = ['Name', 'No_of_guests', 'BookingDate'];
#     filterset_fields =['Name', 'No_of_guests', 'BookingDate'];
#     search_fields =['Name', 'No_of_guests', 'BookingDate'];


# from rest_framework.decorators import api_view

# Create your views here.
# class MenuItemsView(generics.ListCreateAPIView):
# queryset = MenuItem.objects.all()
# serializer_class = MenuItemSerializer

# class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
# queryset = MenuItem.objects.all()
# serializer_class =
