from rest_framework import serializers
from .models import Order



class AddOrderSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Order
        fields = ('id', 'nurseryId', 'userId', 'plantId','quantity','address','phoneNumber','status','orderdAt',)
        extra_kwargs = {'nurseryId': {'required': True}}
        extra_kwargs = {'userId': {'required': True}}
        extra_kwargs = {'plantId': {'required': True}}
        # extra_kwargs = {'totalPrice': {'required': True}}
        extra_kwargs = {'quantity':  {'required': True}}
        extra_kwargs = {'address': {'write_only': True}}
        extra_kwargs = {'phoneNumber': {'required': True}}
        extra_kwargs = {'status': {'required': True}}
        extra_kwargs = {'orderdAt': {'required': True}}

        

      