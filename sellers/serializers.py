
from rest_framework import serializers
from .models import Seller ,Plant


class SellerRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ('id', 'sellername', 'selleremail', 'sellerpass')
        extra_kwargs = {'sellerpass': {'write_only': True}}
        extra_kwargs = {'selleremail': {'required': True,
                                  'allow_blank': False}}
      
 
class SellerLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ('sellername', 'sellerpass')
        extra_kwargs = {'sellerpass': {'write_only': True}}
  

class AddPlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ('id', 'nurseryId', 'plantName', 'plantImage','plantPrice','updatedAt')
        extra_kwargs = {'plantName': {'write_only': True}}
        extra_kwargs = {'nurseryId': {'required': True}}
        extra_kwargs = {'plantImage': {'required': True}}
        extra_kwargs = {'plantPrice': {'required': True}}                          
      


class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ['plantName', 'plantImage', 'plantPrice']