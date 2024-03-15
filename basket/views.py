from django.shortcuts import render


def view_basket(request):
    """ A view that renders the shopping basket contents page """

    return render(request, 'basket/basket.html')