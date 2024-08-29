from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass  # No changes needed, as AbstractUser already has username and password fields

"""class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)"""

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=20)
    image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    address = models.TextField()

    def __str__(self):
        return self.full_name


class CarRent(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    number_plate = models.CharField(max_length=50)
    topspeed = models.IntegerField()
    date_from = models.DateField()
    date_to = models.DateField()
    insurance = models.BooleanField(default=False)
    seats = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image1 = models.ImageField(upload_to='car_images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='car_images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='car_images/', blank=True, null=True)
    image4 = models.ImageField(upload_to='car_images/', blank=True, null=True)
    image5 = models.ImageField(upload_to='car_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.model}"