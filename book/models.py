from django.contrib.auth.models import AbstractUser,Permission
from django.db import models

class CustomUser(AbstractUser):
    user_type = models.CharField(max_length=30, blank=True)
    region_id = models.IntegerField(blank=True, default=None, null=True)


class Userpermissions(models.Model):
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE,  null=True, blank=True)
    user_type = models.CharField(max_length=30)
    is_permission = models.BooleanField(default=False)



class Apartment(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(max_length=100)
    description = models.TextField(max_length=100)
    gst_percent = models.FloatField(blank=True, default=None, null=True)



class Flat(models.Model):
    flat_number = models.CharField(max_length=100)
    address = models.TextField(max_length=100)
    description = models.TextField(max_length=100)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name='flat_apartment', null=True, blank=True)


class AssignedApartment(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name='assigned_apartment', null=True, blank=True)
    user =models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='assigned', null=True, blank=True)
    description = models.TextField(max_length=100)


class Booking (models.Model):
    name = models.CharField(max_length=100)
    user =  models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_booking', null=True, blank=True)
    price = models.FloatField(blank=True, default=None, null=True)
    gst_amount = models.FloatField(blank=True, default=None, null=True)
    total = models.FloatField(blank=True, default=None, null=True)
    flat =  models.ForeignKey(Flat, on_delete=models.CASCADE, related_name='booking_flat', null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)