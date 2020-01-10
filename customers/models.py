from django.db import models
from localflavor.us.models import USZipCodeField, USStateField
from inventory.models import Flower

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=70)
    address_one = models.CharField(max_length=40)
    address_two = models.CharField(max_length=40)
    city = models.CharField(max_length=80)
    state = USStateField()
    zip_code = USZipCodeField()
    date_of_birth = models.DateField(default=21)
    phone = models.IntegerField()
    phone_ext = models.IntegerField()
    email = models.EmailField(max_length=80, null=True)

    class Meta:
        ordering = ['last_name', 'first_name']


class Purchase(models.Model):
    # For amount choices, values are measured in grams.
    ONE_GRAM = 1.
    ONE_EIGHTH = 3.5
    ONE_QUARTER = 7.
    ONE_HALF = 14.
    ONE_OUNCE = 28.

    AMOUNT_CHOICES = [
        (ONE_GRAM, '1 g'),
        (ONE_EIGHTH, '1/8 oz.'),
        (ONE_QUARTER, '1/4 oz.'),
        (ONE_HALF, '1/2 oz.'),
        (ONE_OUNCE, '1 oz.')
    ]

    flower = models.ForeignKey(Flower, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.IntegerField()
    amount = models.DecimalField(max_digits=2, decimal_places=1, choices=AMOUNT_CHOICES)
    purchase_date = models.DateField(auto_now=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-purchase_date', '-amount']
