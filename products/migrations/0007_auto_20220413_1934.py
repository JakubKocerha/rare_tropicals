# Generated by Django 3.2 on 2022-04-13 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_product_all_reviews'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='all_reviews',
        ),
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='productreview',
            name='stars',
        ),
    ]