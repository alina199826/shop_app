from django.contrib import admin
from webapp.models import Product, Category, Order, OrderProduct

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'quantity', 'price', 'category']
    list_filter = ['title']
    exclude = []

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(OrderProduct)
admin.site.register(Order)