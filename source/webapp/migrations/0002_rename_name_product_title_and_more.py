# Generated by Django 5.0.1 on 2024-01-18 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='product',
            name='identification_number',
        ),
    ]
