"""carolscakes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from cakes.views import index
from django.views import static
from django.views.generic import RedirectView
from django.views.static import serve
from products.views import all_products, about, contact, weddingcakes, birthdaycakes, specialoccasion, sheetcakes
from products import urls as urls_products
from accounts import urls as accounts_urls
from search import urls as urls_search
from checkout import urls as urls_checkout
from cart import urls as urls_cart
from .settings import MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^index', index, name='index'),
    url(r'^products', all_products, name='products'),
    url(r'^about', about, name='about'),
    url(r'^contact', contact, name='contact'),
    url(r'^weddingcakes', weddingcakes, name='weddingcakes'),
    url(r'^birthdaycakes', birthdaycakes, name='birthdaycakes'),
    url(r'^specialoccasion', specialoccasion, name='specialoccasion'),
    url(r'^sheetcakes', sheetcakes, name='sheetcakes'),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^products/', include(urls_products)),
    url(r'^cart/', include(urls_cart)),
    url(r'^checkout/', include(urls_checkout)),
    url(r'^search/', include(urls_search)),
]


from django.conf.urls import url, include
from django.contrib import admin
from accounts import urls as urls_accounts
from products import urls as urls_products
from cart import urls as urls_cart
from search import urls as urls_search
from checkout import urls as urls_checkout
from products.views import all_products
from django.views import static
from .settings import MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', all_products, name='index'),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^products/', include(urls_products)),
    url(r'^cart/', include(urls_cart)),
    url(r'^checkout/', include(urls_checkout)),
    url(r'^search/', include(urls_search)),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT})
]