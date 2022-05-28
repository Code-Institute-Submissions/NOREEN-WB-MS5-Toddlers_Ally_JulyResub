"""Imports"""
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

def checkout(request):
    """checkout function"""
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51L4VgeFyGe986LFU700KVGZeE2dUkq4QMY5gTNH8y5CD4saikA9ZPa68cpQDWRG653XdRbRtxdyg5dGfuUkqde3400OW36EHZr',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
