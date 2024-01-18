from rest_framework import serializers
from webapp.models import Category, Product, OrderProduct, Order


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', ]


class ProductItemSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='title', queryset=Category.objects.all())
    id = serializers.ReadOnlyField()
    sum = serializers.ReadOnlyField()

    class Meta:
        model = Product
        fields = ['id', 'title', 'category', 'unit', 'quantity', 'price',
                  'sum']

class OrderProductSerializer(serializers.ModelSerializer):
    total_amount = serializers.SerializerMethodField()

    class Meta:
        model = OrderProduct
        fields = ['product', 'order', 'qty', 'total_amount']

    def get_total_amount(self, obj):
        return obj.total_amount()

    def perform_create(self, serializer):
        instance = serializer.save()
        self.update_product_quantity(instance.product, instance.qty)

    def update_product_quantity(self, product, qty):
        product.quantity -= qty
        product.save()

class OrderSerializer(serializers.ModelSerializer):
    products = OrderProductSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'name', 'phone', 'address', 'created_at', 'products', 'user']