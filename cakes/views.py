from django.shortcuts import render

# Create your views here.
def index(request):
    """
    A view that will show the home page
    """
    return render(request, "index.html")