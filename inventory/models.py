from django.db import models
from localflavor.us.models import USStateField, USZipCodeField
from django.template.defaultfilters import slugify

# Create your models here.
class Grower(models.Model):
    name = models.CharField(max_length=40)
    address_one = models.CharField(max_length=60, blank=True, null=True)
    address_two = models.CharField(max_length=40, blank=True, null=True)
    city = models.CharField(max_length=70)
    state = USStateField()
    zip_code = USZipCodeField()
    email = models.EmailField(max_length=80)
    web_site = models.URLField(max_length=100, blank=True, null=True)
    twitter = models.URLField(max_length=80, blank=True, null=True)
    instagram = models.URLField(max_length=80, blank=True, null=True)
    youtube = models.URLField(max_length=80, blank=True, null=True)

    class Meta:
        ordering = ['name']


    def __str__(self):
        return self.name


class Flower(models.Model):
    FAMILY_CHOICES = [
        ('S', 'Sativa'),
        ('I', 'Indica'),
        ('H', 'Hybrid')
    ]

    strain = models.CharField(max_length=80)
    thc = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='THC')
    family = models.CharField(max_length=6, choices=FAMILY_CHOICES)
    grower = models.ForeignKey(Grower, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True, upload_to='flowers/')
    product_description = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.strain


    # Automatically generates slug based on `strain`.
    def save(self, *args, **kwargs):
        if not self.strain:
            self.slug = slugify(self.strain)
        super(Flower, self).save(*args, **kwargs)
