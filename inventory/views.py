from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404
from django.core.paginator import Paginator
from inventory.models import Flower
from inventory.models import Grower

# Create your views here.
def product_info(request, slug):
    flower = get_object_or_404(Flower, slug=slug)
    return render(request, 'product_info.html', {'flower': flower})


def shop_home(request):
    return render(request, 'shop_home.html')


def flowers_home(request):
    return render(request, 'flowers_home.html')


def growers_home(request):
    grower_list = get_list_or_404(Grower)
    paginator = Paginator(grower_list, 4)  # Show 4 growers per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'growers_home.html',
            {'grower_list': grower_list,
             'page_obj': page_obj,
            })


def grower_info(request, slug):
    grower = get_object_or_404(Grower, slug=slug)
    return render(request, 'grower_info.html', {'grower': grower})
