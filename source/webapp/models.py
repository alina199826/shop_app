from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from . import choices
from django.contrib.auth import get_user_model


class Category(models.Model):
    title = models.CharField(
        _('Категория'),
        max_length=40,
        primary_key=True
    )

    def __str__(self):
        return f' {self.title}'

    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категория товаров')


class Product(models.Model):
    title = models.CharField(
        _('Наименование'),
        max_length=250
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='ProductNormal',
        verbose_name='Категория'

    )

    unit = models.CharField(
        _('Ед.измерения'),
        max_length=9,
        choices=choices.Unit.choices,
        default=choices.Unit.ITEM
    )

    quantity = models.IntegerField(
        _('Кол-во'),
        default=1
    )
    price = models.IntegerField(
        _('Цена'),
    )


    def __str__(self):
        return f'наименование: {self.title}, кол-во: {self.quantity}'

    def get_absolute_url(self):
        return reverse('view', kwargs={'pk': self.pk})


    def save(self, *args, **kwargs):
        self.sum = self.quantity * self.price
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = _('Товар')

class OrderProduct(models.Model):
    product = models.ForeignKey('webapp.Product', on_delete=models.CASCADE, verbose_name='Товар')
    order = models.ForeignKey('webapp.Order', related_name='order_product', on_delete=models.CASCADE, verbose_name='Заказ')
    qty = models.PositiveIntegerField(verbose_name='Количество')

    def __str__(self):
        return f'продукт из заказа: {self.product.title}, кол-во: {self.qty}'

    def total_amount(self):
        return self.product.price * self.qty

    class Meta:
        verbose_name = _('Товар из корзины')

class Order(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Имя пользователя')
    phone = models.CharField(max_length=100, null=False, blank=False, verbose_name='Телефон')
    address = models.CharField(max_length=100, null=False, blank=False, verbose_name='Адрес')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    products = models.ManyToManyField('webapp.Product', related_name='order', through='webapp.OrderProduct',
                                      through_fields=['order', 'product'], verbose_name='Товары')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True, verbose_name='Пользователь')

    def __str__(self):
        return f'заказ {self.name}'


    class Meta:
        verbose_name = _('Заказ')