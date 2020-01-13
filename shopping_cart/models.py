from django.db import models
from accounts.models import Customer
from inventory.models import Flower

# Create your models here.
class ShoppingCart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    flower = models.ManyToManyField(Flower)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    purchase_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-purchase_date', 'customer', ]
