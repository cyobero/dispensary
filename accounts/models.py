import datetime
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from localflavor.us.models import USStateField, USZipCodeField


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True,
                              upload_to='accounts/customers/{}'.format(user))
    bio = models.TextField(max_length=600)
    twitter = models.URLField(max_length=80, blank=True, null=True)
    instagram = models.URLField(max_length=80, blank=True, null=True)
    youtube = models.URLField(max_length=80, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)

    def calculate_age(self):
        current_date = datetime.datetime.today()
        user_birthdate = '%s/%s/%s' % (str(self.birth_date.year),
                                       str(self.birth_date.month), str(self.birth_date.day))
        user_birthdate = datetime.datetime.strptime(user_birthdate, '%Y/%m/%d')
        age = (current_date - user_birthdate)/365.2424
        return age


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.save()


class Plug(models.Model):
    RATINGS_CHOICES = [
        (1, 'Straight Trash'),
        (2, 'Kinda Sketchy'),
        (3, 'Clutch'),
        (4, 'Da Plug'),
        (5, 'El Chapo')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True,
                              upload_to='accounts/customers/{}'.format(user))
    bio = models.TextField(max_length=600)
    twitter = models.URLField(max_length=80, blank=True, null=True)
    instagram = models.URLField(max_length=80, blank=True, null=True)
    youtube = models.URLField(max_length=80, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    address_one = models.CharField(max_length=60, blank=True, null=True)
    address_two = models.CharField(max_length=40, blank=True, null=True)
    city = models.CharField(max_length=70)
    state = USStateField()
    zip_code = USZipCodeField()
    plug_rating = models.IntegerField(
        choices=RATINGS_CHOICES, blank=True, null=True)

    def calculate_age(self):
        current_date = datetime.datetime.today()
        user_birthdate = '%s/%s/%s' % (str(self.birth_date.year),
                                       str(self.birth_date.month), str(self.birth_date.day))
        user_birthdate = datetime.datetime.strptime(user_birthdate, '%Y/%m/%d')
        age = (current_date - user_birthdate)/365.2424
        return age

    class Meta:
        ordering = ['user', '-plug_rating']


@receiver(post_save, sender=User)
def create_plug_profile(sender, instance, created, **kwargs):
    if created:
        Plug.objects.create(user=instance)
