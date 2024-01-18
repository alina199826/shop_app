from django.contrib.auth.mixins import  PermissionRequiredMixin
from webapp.models import Product
from webapp.forms import ProductForm
from django.views.generic import DeleteView, ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy



class IndexViews(ListView):
    context_object_name = 'products'
    model = Product
    ordering = ('category', 'title')



class ProductView(DetailView):
    model = Product


class ProductCreateView(PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    permission_required = 'webapp.add_product'


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    form_class = ProductForm
    model = Product
    context_object_name = 'product'
    permission_required = 'webapp.change_product'



class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('index')
    permission_required = 'webapp.delete_product'

