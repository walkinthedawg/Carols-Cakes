from django.shortcuts import render
from .models import Product

# Create your views here.
def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})
    
def about(request):
    """
    A view that will return a list of posts that were published
    prior to 'now' and render these to the 'boardposts.html
    template.
    """
    return render(request, "about.html")
    
def contact(request):
    """
    A view that will return a list of posts that were published
    prior to 'now' and render these to the 'boardposts.html
    template.
    """
    return render(request, "contact.html")
    
def weddingcakes(request):
    """
    A view that will return a list of posts that were published
    prior to 'now' and render these to the 'boardposts.html
    template.
    """
    products = Product.objects.all()
    return render(request, "weddingcakes.html", {"products": products})
    
def birthdaycakes(request):
    """
    A view that will return a list of posts that were published
    prior to 'now' and render these to the 'boardposts.html
    template.
    """
    products = Product.objects.all()
    return render(request, "birthdaycakes.html", {"products": products})
    
def specialoccasion(request):
    """
    A view that will return a list of posts that were published
    prior to 'now' and render these to the 'boardposts.html
    template.
    """
    products = Product.objects.all()
    return render(request, "specialoccasion.html", {"products": products})
    
def sheetcakes(request):
    """
    A view that will return a list of posts that were published
    prior to 'now' and render these to the 'boardposts.html
    template.
    """
    products = Product.objects.all()
    return render(request, "sheetcakes.html", {"products": products})
    