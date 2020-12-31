from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from users import views
from .views import RegisterAPI , LoginAPI
from knox import views as knox_views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/user/register/', RegisterAPI.as_view(), name='register'),
    path('api/user/login/', LoginAPI.as_view(), name='login'),
    path('api/user/logout/', knox_views.LogoutView.as_view(), name='logout'),
    
]