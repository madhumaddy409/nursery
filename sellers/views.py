from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework import generics, permissions
from . serializers import SellerRegisterSerializer ,SellerLoginSerializer, AddPlantSerializer, PlantSerializer
from rest_framework.response import Response
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import login
from .models import Seller, Plant
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView



# Seller Register API(Nursery register)
class SellerRegisterAPI(generics.GenericAPIView):
    serializer_class = SellerRegisterSerializer

    def post(self, request, *args, **kwargs):
        
        sellerName = request.data['sellername']
        print(sellerName)

        sellerr = Seller.objects.filter(sellername=sellerName)
        print(sellerr)
        if Seller.objects.filter(sellername=sellerName).exists():
            data2 = "Username already taken"
            return Response({
            "seller": data2
    
            })
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            seller = serializer.save()
    
            return Response({
            "seller": SellerRegisterSerializer(seller, context=self.get_serializer_context()).data,
           
            })


# Seller Login API(Nursery login)
class SellerLoginAPI(generics.GenericAPIView):

    permission_classes = (permissions.AllowAny,)
    serializer_class = SellerLoginSerializer

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
       
        sellerName = request.data['sellername']
        print(sellerName)
        sellerpass = request.data['sellerpass']
        print(sellerpass)
        if Seller.objects.filter(sellername=sellerName,sellerpass=sellerpass).exists():
            request.session['username'] = sellerName
            user_name = request.session.get('username')
            
            data = {"login succfully",user_name}
            return Response({
            "seller": data,
            })
        else:
            data = "invalid credential"
            return Response({
            "seller": data
            })
     
        
class SellerprofileAPI(generics.GenericAPIView):

        def get(self, request, format=None):
            user_name = request.session.get('username')
            
            if user_name is not None:
                data = {"u r logged in",user_name}
                return Response({
                "seller": data,
                })
            else:
                data = "invalid credential"
                return Response({
                "seller": data
                })

class AddPlantAPI(generics.GenericAPIView):
    serializer_class = AddPlantSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        plant = serializer.save()
    
        return Response({
        "plant": AddPlantSerializer(plant, context=self.get_serializer_context()).data,
            
        })

class PlantAPI(APIView):
   

    def get(self, request, format=None):
        plants= Plant.objects.all()
        serializer = PlantSerializer(plants, many=True)
        return Response(serializer.data)


class PlantDetailsAPI(APIView):

    def get(self, request, *args, **kwargs):
        plantName =self.kwargs.get('plant')
        print(plantName)
       
        plant = Plant.objects.filter(plantName=plantName).values()

        if plant is not None:  
            
            return Response({
            "plant_details": plant,
            })
        else:
            data = "no such plant here"
            return Response({
            "seller": data
            })

            
     