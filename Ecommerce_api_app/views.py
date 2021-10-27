from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .serializers import ProductSerializer
from rest_framework.views import APIView
from .models import Product


class ProductList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[0:8]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductDetail(APIView):
    pass


