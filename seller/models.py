from unicodedata import category, name
from django.db import models

# Create your models here.

class Add_product(models.Model):
    name = models.CharField(max_length = 50)
    description = models.CharField(max_length= 100)
    category = models.CharField(max_length = 50)
    weight = models.CharField(max_length= 30)
    quantity = models.IntegerField()


class Seller_reg(models.Model):
    name = models.CharField(max_length = 30)
    password = models.CharField(max_length = 20)
    email = models.EmailField(unique = True)
    phone = models.BigIntegerField(unique = True)
    address = models.TextField()


class Product(models.Model):
    name = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits = 20, decimal_places = 2)
    description = models.CharField(max_length = 500)
    image = models.CharField(max_length = 500)
    seller_id = models.ForeignKey(Seller_reg, on_delete = models.CASCADE)
