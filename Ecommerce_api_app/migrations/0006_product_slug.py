# Generated by Django 3.2.8 on 2021-10-28 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce_api_app', '0005_auto_20211022_1709'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=True),
            preserve_default=False,
        ),
    ]
