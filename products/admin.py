from django.contrib import admin

from .models import Category, Product


class ProductAdmin(admin.ModelAdmin):
    """
    Adding extra fields to the product admin page
    """

    list_display = (
        "sku",
        "name",
        "category",
        "price",
        "rating",
        "image",
    )

    ordering = ("sku",)


class CategoryAdmin(admin.ModelAdmin):
    """
    Adding extra fields to the category admin page
    """

    list_display = (
        "friendly_name",
        "name",
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
