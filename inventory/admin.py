from django.contrib import admin
from inventory.models import Flower, Grower, Batch

# Register your models here.
class FlowerAdmin(admin.ModelAdmin):
    ordering = ['strain']
    search_fields = ['strain']
    fields = ('strain', 'grower', 'family', 'thc',
              'image', 'product_description', 'slug')
    list_display = ('strain', 'grower', 'family', 'thc')
    prepopulated_fields = {'slug': ('strain', )}


class GrowerAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_display = ('name', 'city', 'state', 'email', 'slug')
    search_fields = ['name', 'email', 'state', 'city']
    prepopulated_fields = {'slug': ('name', )}


class BatchAdmin(admin.ModelAdmin):
    ordering = ['-harvest_date']
    list_display = ['id', 'harvest_date']

admin.site.register(Flower, FlowerAdmin)
admin.site.register(Grower, GrowerAdmin)
admin.site.register(Batch, BatchAdmin)
