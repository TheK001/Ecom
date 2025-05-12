from django.shortcuts import render, redirect
from .models import Product, Category
from .forms import ProductForm, CategoryForm

def add_product(request):
    categories = Category.objects.all()  # Fetch categories for the dropdown
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products')  # Redirect to the product list after adding the product
        else:
            print(form.errors)  # Debugging: Print form errors to the console
    else:
        form = ProductForm()
    context = {
        'form': form,
        'categories': categories,  # Pass categories to the template
    }
    return render(request, 'add_product.html', context)
        
def list_product(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'product_list.html', context)

from django.contrib import messages

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Category added successfully!")  # Success message
            return redirect('add_category')  # Redirect to the same page to clear POST data
        else:
            messages.error(request, "Failed to add category. Please correct the errors below.")  # Error message
    else:
        form = CategoryForm()
    context = {
        'form': form,
    }
    return render(request, 'add_category.html', context)

def list_category(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'category_list.html', context)