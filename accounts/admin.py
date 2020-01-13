from django.contrib import admin
from accounts.models import Customer, Plug

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    ordering = ['user']
    search_fields = ['user']


class PlugAdmin(admin.ModelAdmin):
    ordering = ['user']
    search_fields = ['user']

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Plug, PlugAdmin)
