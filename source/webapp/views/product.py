from webapp.models import Product
from webapp.forms import ProductForm
from django.views.generic import DeleteView, ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy



class IndexViews(ListView):
    template_name = 'product/index.html'
    context_object_name = 'products'
    model = Product
    ordering = ('category', 'title')



class ProductView(DetailView):
    template_name = 'product/product_view.html'
    model = Product


class ProductCreateView( CreateView):
    template_name = "product/create.html"
    model = Product
    form_class = ProductForm


class ProductUpdateView(UpdateView):
    template_name = "product/product_update.html"
    form_class = ProductForm
    model = Product
    context_object_name = 'product'



class ProductDeleteView(DeleteView):
    model = Product
    template_name = "product/product_delete.html"
    success_url = reverse_lazy('index')

