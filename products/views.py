from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
        context = {
            'form': form,
        }
    return render(request, 'add_product.html', context)
        
def list_product(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'product_list.html', context)

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
        context = {
            'form': form,
        }
    return render(request, 'add_category.html', context)