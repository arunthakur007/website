from django.db import models

# Create your models here.


class order(models.Model):
    items_name=models.CharField(max_length=200)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    total=models.DecimalField(max_digits=10, decimal_places=2)
    amount= models.DecimalField(max_digits=8, decimal_places=2)

class user(models.Model):
    user_information=models.CharField(max_length=200)

