from django.contrib import admin
from shopping_cart.models import ShoppingCart

# Register your models here.
class ShoppingCartAdmin(admin.ModelAdmin):
    ordering = ['customer', '-purchase_date']
    list_display = ['customer', 'purchase_date', 'quantity', 'unit_price']
    search_fields = ['customer', 'purchase_date']

admin.site.register(ShoppingCart, ShoppingCartAdmin)
