from django.shortcuts import render
from django.shortcuts import get_object_or_404
from inventory.models import Flower

# Create your views here.
def product_info(request, slug):
    flower = get_object_or_404(Flower, slug=slug)
    return render(request, 'product_info.html', {'flower': flower})


def shop_home(request):
    return render(request, 'shop_home.html')
