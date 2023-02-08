"""LittleLemon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

## Add
from rest_framework.routers import DefaultRouter

# import obtain_auth_token view
from rest_framework.authtoken.views import obtain_auth_token


from LittleLemonAPI.views import SingleMenuItemView, MenuItemsView;

### ADD ###
from LittleLemonAPI.views import bookings, index;



router = DefaultRouter()
# urlpatterns = [
#     path('restaurant/booking/', include(router.urls)),
#     path('restaurant/booking/tables', include(router.urls)),
# ]

urlpatterns = [
    path("admin/", admin.site.urls),
    
    # path("menu/", MenuItemsView.as_view()),
    path('menu/', MenuItemsView, name='menu-list'),
    path("menu/<int:pk>", SingleMenuItemView.as_view()),
    
    # add following line to urlpatterns list
    # path('restaurant/menu/', include('restaurant.urls')),
    path("LittleLemonAPI/", include("LittleLemonAPI.urls")),
    # path(".", include("LittleLemonAPI.urls")),
    #
    path("LittleLemonAPI/booking/", include(router.urls)),
    path("LittleLemonAPI/booking/tables", include(router.urls)),
    # add following lines to update urlpatterns list
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
    # add following line in urlpatterns list
    path("api-token-auth/", obtain_auth_token),
    # path('menu-items/', '.'),
    path("api-token-auth/", obtain_auth_token),
    
    path("api/menu-items/", MenuItemsView),
    path("api/menu-items/<int:pk>", SingleMenuItemView.as_view()),
    
    
    path('bookings', bookings, name='bookings'), 
    
    ### ADD statics routes ###
    path('', index, name='index'),
    
]
