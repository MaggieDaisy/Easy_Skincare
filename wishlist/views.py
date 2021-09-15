from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from products.models import Product
from profiles.models import UserProfile

from wishlist.models import Wishlist


@login_required
def wishlist(request):
    profile = UserProfile.objects.get(user=request.user)
    wishlisted_products = [
        wishlist_entry.product
        for wishlist_entry in Wishlist.objects(
            user_profile=profile,
        )
    ]

    return render("wishlist.html", {"products": wishlisted_products})


@login_required
def add_to_wishlist(request, item_id):
    """A view that allows users to add a specified
    product to the wishlist"""

    product = get_object_or_404(Product, pk=item_id)
    redirect_url = request.POST.get("redirect_url")

    profile = UserProfile.objects.get(user=request.user)
    wishlist_entry = Wishlist(
        user_profile=profile,
        product=product,
    )
    wishlist_entry.save()
    messages.success(request, f"Added {product.name} to your wishlist")

    return redirect(redirect_url)
