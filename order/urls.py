from django.contrib import admin
from django.urls import include, path 
from rest_framework import routers
from users import views
from .views import AddOrderAPI, OredrDetailsAPI

from django.conf.urls import include, url


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [


    path('api/order/addorder/', AddOrderAPI.as_view(), name='register'),
    url(r'^api/order/(?P<sellername>.*)/$',OredrDetailsAPI.as_view(), name='plant'),
 
]