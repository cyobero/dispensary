from django.contrib import admin
from inventory.models import Flower, Grower

# Register your models here.
class FlowerAdmin(admin.ModelAdmin):
    ordering = ['strain']
    search_fields = ['strain']
    fields = ('strain', 'grower', 'family', 'thc', 'image', 'product_description', 'slug')
    list_display = ('strain', 'grower', 'family', 'thc')
    prepopulated_fields = {'slug': ('strain', )}

class GrowerAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_display = ('name', 'city', 'state', 'email')
    search_fields = ['name', 'email', 'state', 'city']

admin.site.register(Flower, FlowerAdmin)
admin.site.register(Grower, GrowerAdmin)
