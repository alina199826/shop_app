from django.db import models
from django.utils.translation import gettext_lazy as _
from . import choices


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
    sum = models.IntegerField(
        _('Сумма'),
        default=0
    )

    def __str__(self):
        return f'наименование: {self.title}, кол-во: {self.quantity}'

    def save(self, *args, **kwargs):
        self.sum = self.quantity * self.price
        return super().save(*args, **kwargs)