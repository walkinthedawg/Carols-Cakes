from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):
    """
    A view that will return the index.html template.
    """
    return render(request, "index.html")
    
def all_products(request):
    """
    A view that will return a list of all products to the products.html template.
    """
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})
    
def about(request):
    """
    A view that will return to the about.html template.
    """
    return render(request, "about.html")
    
def contact(request):
    """
    A view that will return to the contact.html template.
    """
    return render(request, "contact.html")
    
def weddingcakes(request):
    """
    A view that will return a list of cakes to the weddingcakes.html template.
    """
    products = Product.objects.all()
    return render(request, "weddingcakes.html", {"products": products})
    
def birthdaycakes(request):
    """
    A view that will return a list of birthday cakes to the birthdaycakes.html template.
    """
    products = Product.objects.all()
    return render(request, "birthdaycakes.html", {"products": products})
    
def specialoccasion(request):
    """
    A view that will return a list of special occasion cakes to the specialoccasion.html template.
    """
    products = Product.objects.all()
    return render(request, "specialoccasion.html", {"products": products})
    
def sheetcakes(request):
    """
    A view that will return a list of sheetcakes to the sheetcakes.html template.
    """
    products = Product.objects.all()
    return render(request, "sheetcakes.html", {"products": products})
    
def search(request):
    """
    A view that will return a list of search results to the search.html template.
    """
    return render(request, "search.html")
    