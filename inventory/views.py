from django.shortcuts import render
from inventory.models import

# Create your views here.
def product_info(request):
    return render(request, 'product_info.html')
