from django.conf.urls import url, include
from .views import all_products, search


urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^$', search, name='search'),
    
]