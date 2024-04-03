from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from products.models import Artist, Product
from .forms import ArtistForm

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


@login_required
def add_artist(request):
    """ Add an artist to the database """
    if not request.user.is_superuser and request.user.is_anonymous:
        messages.error(request, 'Ooops! Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    # else:
    #     if request.user.is_anonymous:
    #         messages.error(request, 'Ooops! Sorry, only store owners can do that.')
    #     return redirect(reverse('home'))

    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES)
        if form.is_valid():
            artist = form.save()
            messages.success(request, 'Success! The artist was added to the database.')
            return redirect(reverse('artists'))
        else:
            messages.error(request, 'Failed to add artist. Please ensure the form is valid.')
    else:
        form = ArtistForm()
        
    template = 'artists/add_artist.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_artist(request, artist_id):
    """ Make changes to an artist in the database """
    if not request.user.is_superuser:
        messages.error(request, 'Ooops! Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    artist = get_object_or_404(Artist, pk=artist_id)
    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES, instance=artist)
        if form.is_valid():
            form.save()
            messages.success(request, f'Success! You have updated the profile of {artist.name}.')
            return redirect(reverse('artist_detail', args=[artist.id]))
        else:
            messages.error(request, 'Failed to update artist. Please ensure the form is valid.')
    else:
        form = ArtistForm(instance=artist)
        messages.info(request, f'You are editing the profile of {artist.name}')

    template = 'artists/edit_artist.html'
    context = {
        'form': form,
        'artist': artist,
    }

    return render(request, template, context)
