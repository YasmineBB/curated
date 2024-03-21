from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product

def view_basket(request):
    """ A view that renders the shopping basket contents page """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ A view that adds a specified product to the shopping basket """


    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        messages.error(request, f'There is only one of {product.name} and you already have it in your basket!')
    else:
        basket[item_id] = quantity
        messages.success(request, f'Added {product.name} to your basket')
        
    request.session['basket'] = basket
    return redirect(redirect_url)


def remove_from_basket(request, item_id):
    """A view that removes a specified item from the shopping basket"""

    basket = request.session.get("basket", {})
    product = get_object_or_404(Product, pk=item_id)

    if basket[item_id]:
        basket.pop(item_id)
        messages.success(request, f'Removed {product.name} from your basket')

        request.session['basket'] = basket 
        return HttpResponse(status=200)
