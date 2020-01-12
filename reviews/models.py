from django.db import models
from inventory.models import Flower
from inventory.models import Grower
from multiselectfield import MultiSelectField

# Create your models here.
class Review(models.Model):
    RATINGS_CHOICES = [
        (1, 'Doo-doo'), (2, 'Reggie Miller'),
        (3, 'Decent'),
        (4, 'Bomb'),
        (5, 'GOAT')
    ]

    REPORTED_FEELINGS_CHOICES = [
        (1, 'Happy'),
        (2, 'Relaxed'),
        (3, 'Sleepy'),
        (5, 'Anxious'),
        (6, 'Paranoid'),
        (7, 'Creative'),
        (8, 'Energized'),
    ]

    REPORTED_EFFECTS_CHOICES = [
        (1, 'Couchlocked'),
        (2, 'Munchies'),
        (3, 'Giggles'),
        (4, 'Low key kinda aroused'),
        (5, 'Body High'),
    ]

    # What kind of activities go well with this strain?
    ACTIVITIES_CHOICES = [
        (1, 'Watching Movies'),
        (2, 'Arts & Crafts'),
        (3, 'Nature Walks'),
        (4, 'Reading/Writing'),
        (5, 'Lounging'),
    ]

    RELIEVES_CHOICES = [
        (1, 'Chronic Pain'),
        (2, 'Anxiety'),
        (3, 'Stress'),
        (4, 'Depression')
    ]

    rating = models.IntegerField(choices=RATINGS_CHOICES, blank=True, null=True)
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE)
    review = models.TextField(blank=True, null=True, default='Not yet reviewed.')
    reported_feelings = MultiSelectField(choices=REPORTED_FEELINGS_CHOICES, max_choices=8, blank=True, null=True)
    reported_effects = MultiSelectField(choices=REPORTED_EFFECTS_CHOICES, max_choices=4, blank=True, null=True)
    reported_activities = MultiSelectField(choices=ACTIVITIES_CHOICES, max_choices=4, blank=True, null=True)
    reported_reliefs = MultiSelectField(choices=RELIEVES_CHOICES, max_choices=4, blank=True, null=True)


    class Meta:
        ordering = ['-rating', 'flower']
