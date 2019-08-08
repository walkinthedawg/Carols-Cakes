from django.shortcuts import render

# Create your views here.
def index(request):
    """
    A view that will return a list of posts that were published
    prior to 'now' and render these to the 'boardposts.html
    template.
    """
    return render(request, "index.html")