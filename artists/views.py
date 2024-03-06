from django.shortcuts import render
from products.models import Artist, Product

# Create your views here.

def all_artists(request):
    """ A view to display all artists """

    artists = Artist.objects.all()

    context = {
        'artists': artists,
    }

    return render(request, 'artists/artists.html', context)
