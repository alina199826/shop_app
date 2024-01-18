from rest_framework import generics
from webapp.models import Category, Product, Order, OrderProduct
from .serializers import CategorySerializer, ProductItemSerializer, OrderSerializer, OrderProductSerializer

class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductItemSerializer

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductItemSerializer

class OrderListView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderProductListView(generics.ListCreateAPIView):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer

class OrderProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        self.update_product_quantity(instance.product, instance.qty)

    def update_product_quantity(self, product, qty):
        product.quantity -= qty
        product.save()