from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework import generics, permissions
from . serializers import AddOrderSerializer
from rest_framework.response import Response


from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from sellers.models import Plant ,Seller
from .models import Order

# Register API
class AddOrderAPI(generics.GenericAPIView):
    serializer_class = AddOrderSerializer

    def post(self, request, *args, **kwargs):
 
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        addorder = serializer.save()
        quantity = request.data['quantity']
        plantId = request.data['plantId']
        userId = request.data['userId']
        nurseryId = request.data['nurseryId']
        plant = Plant.objects.get(id=plantId).plantPrice
        plantName = Plant.objects.get(id=plantId).plantName

        plantPrice = int(plant)
        totalPrice = plantPrice * int(quantity)
        Order.objects.filter(nurseryId=nurseryId,plantId=plantId,userId=userId).update(totalPrice=totalPrice,plantName=plantName)

        return Response({
        "order": AddOrderSerializer(addorder, context=self.get_serializer_context()).data,
      
 
        })



class OredrDetailsAPI(APIView):

    def get(self, request, *args, **kwargs):
        sellername =self.kwargs.get('sellername')
        print(sellername)

        sellerId = Seller.objects.get(sellername = sellername).id
        print(sellerId)
       
        order = Order.objects.filter(nurseryId=sellerId).values()


        if order is not None:  
            
            return Response({
            "order_details": order
            # "plant details":plant

            })
        else:
            data = "there is orders"
            return Response({
            "seller": data
            })