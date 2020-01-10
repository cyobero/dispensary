from django.contrib import admin
from inventory.models import Flower, Grower

# Register your models here.
class FlowerAdmin(admin.ModelAdmin):
    pass

class GrowerAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'state', 'email')

admin.site.register(Flower, FlowerAdmin)
admin.site.register(Grower, GrowerAdmin)
