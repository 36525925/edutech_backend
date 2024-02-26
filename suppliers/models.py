import datetime

from django.db import models

# Create your models here.
from django.db import models

class Suppliers(models.Model):
    businessName = models.CharField(max_length=255)
    supplierNO = models.CharField(max_length=255)
    prefix = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=255)
    altPhone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    dob = models.CharField(max_length=255)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postalCode = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    openingBalance = models.CharField(max_length=255)
    payTerm = models.CharField(max_length=255)
    payCategory = models.CharField(max_length=255)
    dateCreated = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'suppliers'

    def _str_(self):
        return self.businessName