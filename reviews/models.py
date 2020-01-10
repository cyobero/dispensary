from django.db import models
from inventory.models import Flower
from inventory.models import Grower

# Create your models here.
class Reviews(models.Model):
    RATINGS_CHOICES = [
        (1, 'Doo-doo'),
        (2, 'Reggie Miller'),
        (3, 'Decent'),
        (4, 'Bomb'),
        (5, 'GOAT')
    ]

    rating = models.IntegerField(choices=RATINGS_CHOICES)
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE)
    grower = models.ForeignKey(Grower, on_delete=models.CASCADE)
