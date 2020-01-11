"""dispensary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from dispensary.views import home
from inventory.views import product_info
from inventory.views import grower_info
from inventory.views import shop_home
from inventory.views import flowers_home
from inventory.views import growers_home
from dispensary import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('shop/', shop_home, name='shop_home'),
    path('shop/flowers/', flowers_home, name='flowers_home'),
    path('shop/flowers/<slug:slug>', product_info, name='product_info'),
    path('growers/', growers_home, name='growers_home'),
    path('growers/<slug:slug>', grower_info, name='grower_info')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
