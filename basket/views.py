from django.shortcuts import render, redirect


def view_basket(request):
    """ A view that renders the shopping basket contents page """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add a quantity of the specified product to the shopping basket """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity
        
    request.session['basket'] = basket
    return redirect(redirect_url)


# def add_to_basket(request, item_id):
#     """ Add a quantity of the specified product to the shopping basket """

#     quantity = int(request.POST.get('quantity'))
#     redirect_url = request.POST.get('redirect_url')
#     basket = request.session.get('basket', {})

#     if item_id in list(basket.keys()):
#         basket[item_id] = quanitity
#     else:
#         request.session['basket'] = basket
#         return redirect(redirect_url)
        

#     request.session['basket'] = basket
#     print(request.session['basket', {}])
#     return redirect(redirect_url)