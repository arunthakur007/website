from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class store_information(models.Model):
    store=models.CharField(max_length=100)

    def __str__(self):
        return self.store

ORDER_STATUS_CHOICES = (
    ('placed','Placed'),
    ('packed','Packed'),
    ('transit', 'Transit'),
    ('delivered',' Delivered'),
)
class Order(models.Model):
    store = models.ForeignKey(store_information, on_delete=models.CASCADE)
    items_name=models.CharField(max_length=200)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    total=models.DecimalField(max_digits=10, decimal_places=2)
    amount= models.DecimalField(max_digits=8, decimal_places=2)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    create_data = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=9, choices=ORDER_STATUS_CHOICES, default='placed')


    def __str__(self):
        return self.items_name

class user_information(models.Model):
    order_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    phone = models.CharField(max_length=20)



class store_item(models.Model):
    store = models.ForeignKey(store_information, on_delete=models.CASCADE)
    items_name = models.CharField(max_length=200)
    total= models.DecimalField(max_digits=10, decimal_places=2)
    price=models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return str(self.store) + " : " + self.items_name






