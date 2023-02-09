from django import forms

from .models import Product


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]


class RawProductForm(forms.Form):
    title = forms.CharField(label='Title', widget=forms.TextInput(
        attrs={
            "placeholder": "Your Title"
        }
    ))
    description = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "new-class-name two",
            "rows": 10,
            "cols": 20
        })
    )
    price = forms.DecimalField(max_digits=20, decimal_places=2, initial=199.99)
