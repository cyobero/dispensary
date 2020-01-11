from django.contrib import admin
from reviews.models import Review

# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    ordering = ['rating']

admin.site.register(Review, ReviewAdmin)
