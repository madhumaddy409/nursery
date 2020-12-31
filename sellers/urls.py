from django.contrib import admin
from django.urls import include, path 
from rest_framework import routers
from users import views
from .views import SellerRegisterAPI ,SellerLoginAPI ,SellerprofileAPI, AddPlantAPI, PlantAPI, PlantDetailsAPI
from knox import views as knox_views
from django.conf.urls import include, url


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [


    path('api/nursery/register/', SellerRegisterAPI.as_view(), name='register'),
    path('api/nursery/login/', SellerLoginAPI.as_view(), name='login'),
    path('api/nursery/profile/', SellerprofileAPI.as_view(), name='profile'),
    path('api/nursery/addplant/',AddPlantAPI.as_view(), name='addplant'),
    path('api/nursery/plants/',PlantAPI.as_view(), name='plant'),
    url(r'^api/nursery/plants/(?P<plant>.*)/$',PlantDetailsAPI.as_view(), name='plant'),
]