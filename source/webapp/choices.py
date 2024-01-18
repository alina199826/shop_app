from django.db import models


class Unit(models.TextChoices):
    """Ед.измерения"""
    ITEM = 'item', 'шт'
    KILOGRAM = 'killogram', 'кг'
    LITER = 'litr', 'литр'


