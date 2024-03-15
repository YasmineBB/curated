from django.shortcuts import render, get_object_or_404
from products.models import Artist, Product

# Create your views here.

def all_artists(request):
    """ A view to display all artists """

    artists = Artist.objects.all()

    context = {
        'artists': artists,
    }

    return render(request, 'artists/artists.html', context)


def artist_detail(request, artist_id):
    """ A view to display individual artist profile """

    artist = get_object_or_404(Artist, pk=artist_id)

    context = {
        'artist': artist,
    }

    return render(request, 'artists/artist_detail.html', context)
