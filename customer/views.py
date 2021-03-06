"""Imports"""
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import ContactForm


# Create your views here.
def contact(request):
    """ A view to handle the customer contact form """

    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for contacting us. We will \
                be in touch shortly.')
            return redirect(reverse('contact'))

    context = {
        'form': form
    }

    return render(request, 'customer/contact.html', context)


def privacy_policy(request):
    """ A view to handle the privacy policy page """
    return render(request, 'customer/privacy-policy.html')
