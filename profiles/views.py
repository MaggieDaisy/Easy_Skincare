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

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = "profiles/profile.html"
    context = {
        "form": form,
        "profile": profile,
        "orders": orders,
    }

    return render(request, template, context)
