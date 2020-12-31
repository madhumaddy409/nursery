from django.db import models

# Create your models here.
class Seller(models.Model):
    id = models.AutoField(primary_key=True)
    sellername = models.CharField(max_length=60, blank=False)
    selleremail = models.CharField(max_length=60,  blank=False)
    sellerpass = models.CharField(max_length=250, blank=False)


class Plant(models.Model):
    id = models.AutoField(primary_key=True)
    nurseryId = models.ForeignKey(Seller, on_delete=models.CASCADE, default="")
    plantName = models.CharField(max_length=60, blank=False)
    plantImage = models.CharField(max_length=350,  blank=False)
    plantPrice = models.DecimalField(decimal_places=4,max_digits=30, blank=False)
    updatedAt = models.DateTimeField(auto_now_add=True, blank=True)