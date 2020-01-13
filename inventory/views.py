from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from django.core.paginator import Paginator
from inventory.models import Flower
from inventory.models import Grower

# Create your views here.
def product_info_view(request, slug):
    flower = get_object_or_404(Flower, slug=slug)
    return render(request, 'product_info.html', {'flower': flower})


def shop_home_view(request):
    return render(request, 'shop_home.html')


def flowers_home_view(request):
    flowers_list = get_list_or_404(Flower)
    paginator = Paginator(flowers_list, 6)  # Show 6 flowers per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'flowers_home.html', {'flowers_list': flowers_list})


def growers_home_view(request):
    growers_list = get_list_or_404(Grower)
    paginator = Paginator(growers_list, 4)  # Show 4 growers per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'growers_home.html',
            {'growers_list': growers_list,
             'page_obj': page_obj,
            })


def grower_info_view(request, slug):
    grower = get_object_or_404(Grower, slug=slug)
    return render(request, 'grower_info.html', {'grower': grower})
