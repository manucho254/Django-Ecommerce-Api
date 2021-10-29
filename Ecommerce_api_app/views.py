from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.views import APIView
from django.http import Http404
from .models import Category, Product


class ProductList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[0:8]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductDetail(APIView):
    def get_object(self, product_category_slug, product_slug):
        try:
            return Product.objects.filter(product_category__slug=product_category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, product_category_slug, product_slug, format=None):
        product = self.get_object(product_category_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

class CategoryDetail(APIView):
    def get_object(self, product_category_slug):
        try:
            return Category.objects.get(slug=product_category_slug)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, product_category_slug, format=None):
        category = self.get_object(product_category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
