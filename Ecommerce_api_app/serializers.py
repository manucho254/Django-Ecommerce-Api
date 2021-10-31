from rest_framework import serializers
from .models import Category,  Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id',
            'product_vendor',
            'product_name',
            'get_absolute_url',
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

class  CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = [
            'id',
            'category_name',
            'get_absolute_url',
            'products'
        ]




