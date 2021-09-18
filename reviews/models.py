from django.db import models
from products.models import Product
from profiles.models import UserProfile

# Create your models here.


class Review(models.Model):
    """
    A model that allows a user to leave a review for the product
    """

    product = models.ForeignKey(
        Product, related_name="reviews", on_delete=models.CASCADE
    )
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
