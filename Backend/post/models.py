from django.db import models

# Create your models here.


class RegistrationAdmin(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=50)

class Registration(models.Model):
    dealerName = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    city = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    new_after = models.CharField(max_length=255)
    new_minimum = models.IntegerField()
    new_existing = models.BooleanField(default=False)
    new_per_veh = models.CharField(max_length=255)
    new_upload = models.FileField(upload_to="")
    used_after = models.CharField(max_length=255)
    used_minimum = models.IntegerField()
    used_existing = models.BooleanField(default=False)
    used_per_veh = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    used_upload = models.FileField(upload_to="")
    
    def __str__(self):
        return self.dealerName