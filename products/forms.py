from django import forms
from .models import Product, Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock', 'image', 'category']
    
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']