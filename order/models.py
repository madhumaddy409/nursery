from django.db import models
from sellers.models import Seller, Plant
from django.contrib.auth.models import User


# Create your models here.
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    nurseryId = models.ForeignKey(Seller, on_delete=models.CASCADE, default="")
    userId = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    plantId = models.ForeignKey(Plant, on_delete=models.CASCADE, default="")

    plantName = models.CharField(max_length=800, null=True, blank=True)
    totalPrice = models.DecimalField(decimal_places=4,max_digits=30,null=True, blank=True)
    quantity = models.BigIntegerField(blank=False)

    
    address = models.CharField(max_length=800, blank=False)
    
    phoneNumber = models.CharField(max_length=25,blank=False)
    status = models.CharField(max_length=50,blank=False)
    
    
    orderdAt = models.DateTimeField(auto_now_add=True, blank=False)

    