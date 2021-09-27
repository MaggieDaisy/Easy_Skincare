from django.db import models
from products.models import Product
from profiles.models import UserProfile


class Wishlist(models.Model):
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="wishlists",
    )
    products = models.ManyToManyField(Product)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Wishlist ({self.user_profile})"
