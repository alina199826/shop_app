# Generated by Django 5.0.1 on 2024-01-18 17:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('title', models.CharField(max_length=40, primary_key=True, serialize=False, verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категория товаров',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Наименование')),
                ('identification_number', models.CharField(max_length=200, unique=True, verbose_name='ID')),
                ('unit', models.CharField(choices=[('item', 'шт'), ('killogram', 'кг'), ('litr', 'литр')], default='item', max_length=9, verbose_name='Ед.измерения')),
                ('quantity', models.IntegerField(default=1, verbose_name='Кол-во')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('sum', models.IntegerField(default=0, verbose_name='Сумма')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ProductNormal', to='webapp.category')),
            ],
        ),
    ]
