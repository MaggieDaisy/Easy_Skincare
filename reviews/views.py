from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render, reverse
from products.models import Product
from profiles.models import UserProfile

from .forms import ReviewForm
from .models import Review


@login_required
def add_review(request, product_id):
    """
    Add a review to a specific product
    """
    product = get_object_or_404(Product, pk=product_id)
    user = get_object_or_404(UserProfile, user=request.user)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data["content"]
            Review.objects.create(
                user=user,
                product=get_object_or_404(Product, pk=product_id),
                content=content,
            )
            messages.success(request, "Your review was successfuly added.")
            return redirect(reverse("product_detail", args=[product_id]))
        else:
            messages.error(
                request,
                "Failed to add review. \
                    Please check the form is valid and try again.",
            )
    else:
        form = ReviewForm()
    template = "reviews/add_review.html"
    context = {
        "form": form,
        "product": product,
    }

    return render(request, template, context)
