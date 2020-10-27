from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . models import TdtProduct, TdtColor
# Create your views here.

class ProductListView(ListView):
    template_name = 'store.html'
    model = TdtProduct
    context_object_name = 'product'
    