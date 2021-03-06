# Generated by Django 3.2.8 on 2021-10-22 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce_api_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='date',
            new_name='created_date',
        ),
        migrations.AddField(
            model_name='product',
            name='product_description',
            field=models.TextField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
