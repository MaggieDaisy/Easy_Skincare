from django.contrib import messages
from django.shortcuts import redirect, render, reverse

from .forms import OrderForm

# Create your views here.


def checkout(request):
    bag = request.session.get("bag", {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse("products"))

    order_form = OrderForm()
    template = "checkout/checkout.html"
    context = {
        "order_form": order_form,
        "stripe_public_key": "pk_test_51JPt7YBZB2qLq1XaEYfPFTFuJDmd8gLTl9vrNZN5FOoKYsXPGkKZygJs6lERGgjMXI2fEaFAVFh6NyLRZv4G5hk200fKUmRlKQ",
        "client_secret": "test client secret",
    }

    return render(request, template, context)
