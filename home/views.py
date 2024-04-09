from django.shortcuts import render


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def privacy(request):
    """
    A view that returns the privacy policy page
    """
    return render(request, "home/privacy.html")


def about(request):
    """
    A view that returns the about page
    """
    return render(request, "home/about.html")
