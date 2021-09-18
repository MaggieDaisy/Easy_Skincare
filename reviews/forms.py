from django import forms

from .models import Review


class ReviewForm(forms.ModelForm):
    """
    Form for users to add reviews
    """

    class Meta:
        model = Review
        exclude = (
            "user",
            "date_posted",
            "product",
        )

        fields = ["content"]
