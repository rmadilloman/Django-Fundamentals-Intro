from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product

# List all the products
class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'

# Show one product detail
class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'

# Create a new product
# reverse lazy to redirect back, its neat
class ProductCreateView(CreateView):
    model = Product
    template_name = 'product_form.html'
    fields = ['name', 'price', 'description', 'seller', 'color', 'product_dimensions']
    success_url = reverse_lazy('product_list')

# Update the existing product
class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product_form.html'
    fields = ['name', 'price', 'description', 'seller', 'color', 'product_dimensions']
    success_url = reverse_lazy('product_list')

# Delete product
class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('product_list')