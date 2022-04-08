from django.forms import ModelForm
from .models import Products


class ProductForm(ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'weight', 'color']
