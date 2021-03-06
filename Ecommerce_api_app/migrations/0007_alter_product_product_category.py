# Generated by Django 3.2.8 on 2021-11-01 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce_api_app', '0006_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='Ecommerce_api_app.category'),
        ),
    ]
