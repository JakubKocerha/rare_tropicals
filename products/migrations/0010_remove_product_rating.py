# Generated by Django 3.2 on 2022-04-25 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_product_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
    ]