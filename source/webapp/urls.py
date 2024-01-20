from accounts.views import RegisterView
from .views.product import IndexViews, ProductCreateView, ProductDeleteView, ProductView, ProductUpdateView
from .views.cart import CartList, CartDelete, OrderCreate, OrderList, CartDeleteOne, AddItemToCart
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path


urlpatterns = [
    path('', IndexViews.as_view(), name='index'),
    path('product/add/', ProductCreateView.as_view(), name='create'),
    path('product/<int:pk>/', ProductView.as_view(), name='view'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='delete'),
    path('product/<int:pk>/ad_to_cart/', AddItemToCart.as_view(), name='add_to_cart'),
    path('cart/', CartList.as_view(), name='cart_index'),
    path('cart/<str:pk>/delete/', CartDelete.as_view(), name='cart_delete'),
    path('cart/<str:pk>/delete/one', CartDeleteOne.as_view(), name='cart_delete_one'),
    path('order/', OrderCreate.as_view(), name='order_create'),
    path('orders/', OrderList.as_view(), name='order_list'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', RegisterView.as_view(), name='user_create'),

]
