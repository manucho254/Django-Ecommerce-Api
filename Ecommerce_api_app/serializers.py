from django.db.models import fields
from rest_framework import serializers
from .models import Category,  Product


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'category_name'
        )
        model = Category

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id',
            'product_vendor',
            'product_name',
            'get_product_image',
            'get_product_thumbnail',
            'product_category',
            'product_price',
            'stock',
            'description',
            'status',
            'created_date',
        )
        model = Product






