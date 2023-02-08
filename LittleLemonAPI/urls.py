from django.contrib import admin
from django.urls import path, include

### ADD ###
from .views import SingleMenuItemView, BookingViewSet, MenuItemsView, bookings, index;
from rest_framework.routers import DefaultRouter;


# from rest_framework import routers;

router = DefaultRouter()
router.register("arduino", BookingViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    # add following lines to urlpatterns list
    # path("menu/", MenuItemView.as_view()),
    # path("menu/<int:pk>", SingleMenuItemView.as_view()),
    # path("menu-items/", MenuItemsView.as_view()),
    
    
    # path("menu-items/", MenuItemviewAPI.as_view()),
    
    path('bookings', bookings, name='bookings'), 
    
    ### ADD statics routes ###
    path('', index, name='index'),
]
