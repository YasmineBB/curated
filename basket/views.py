from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

from products.models import Product

def view_basket(request):
    """ A view that renders the shopping basket contents page """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ A view that adds a specified product to the shopping basket """


    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        messages.success(request, f'Added {product.name} to your basket')
    else:
        basket[item_id] = quantity
        messages.success(request, f'Added {product.name} to your basket')
        
    request.session['basket'] = basket
    return redirect(redirect_url)


def remove_from_basket(request, item_id):
    """A view that removes a specified item from the shopping basket"""

    basket = request.session.get("basket", {})

    if basket[item_id]:
        basket.pop(item_id)

        request.session['basket'] = basket 
        return HttpResponse(status=200)
