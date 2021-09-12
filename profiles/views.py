from checkout.models import Order
from django.contrib import messages
from django.shortcuts import get_object_or_404, render

from .forms import UserProfileForm
from .models import UserProfile


def profile(request):
    """A view that display the user's profile"""
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully")
        else:
            messages.error(
                request, "Update failed. Please ensure the form is valid."
            )
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = "profiles/profile.html"
    context = {"form": form, "orders": orders, "on_profile_page": True}

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(
        request,
        (
            f"This is past confirmation for order number { order_number}. "
            "A confirmation email was sent on the order date."
        ),
    )

    template = "checkout/checkout_success.html"
    context = {
        "order": order,
        "form_profile": True,
    }

    return render(request, template, context)
