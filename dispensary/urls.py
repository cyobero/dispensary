"""dispensary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home_view, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home_view')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from dispensary.views import home_view
from inventory.views import product_info_view
from inventory.views import grower_info_view
from inventory.views import shop_home_view
from inventory.views import flowers_home_view
from inventory.views import growers_home_view
from accounts.views import register_view
from accounts.views import login_view
from reviews.views import review
from dispensary import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home_view'),
    path('shop/', shop_home_view, name='shop_home_view'),
    path('shop/flowers/', flowers_home_view, name='flowers_home_view'),
    path('shop/flowers/<slug:slug>', product_info_view, name='product_info_view'),
    path('growers/', growers_home_view, name='growers_home_view'),
    path('growers/<slug:slug>', grower_info_view, name='grower_info_view'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', login_view, name='login_view'),
    path('register_view/', register_view, name='register_view'),
    path('reviews/<slug:slug>', review, name='review_view'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
