from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone = models.CharField(null=True, blank=True,unique=True, max_length=20)
    address = models.TextField()

class RepairRequest(models.Model):
    item_name = models.CharField(max_length=255)
    description = models.TextField()
    pickup_address = models.TextField()
    offer_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item_name

class ItemImage(models.Model):
    request = models.ForeignKey(RepairRequest, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='repair_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
