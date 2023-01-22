
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51MSNYIJAHRIfZ4VhR4g92WezqXKpVEznUqSKeHm993Jttxy5i6C4ICQ58cN4nk7grZpXwnD5ieha8jPAPbi7Y4IQ00FcECIm21',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)