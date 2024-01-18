from django import forms
from webapp.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title',  'price', 'category', 'unit', 'quantity', 'sum']




