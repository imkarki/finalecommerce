# Generated by Django 5.1.4 on 2025-02-12 08:13

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_remove_orderplaced_o_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
