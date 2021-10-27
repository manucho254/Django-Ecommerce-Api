from django.urls import path
from .views import ProductList,ProductDetail

urlpatterns = [
    path('product/',  ProductList.as_view(), name="products"),
    path('product/<slug:category_slug>/<slug:product_slug>/',  ProductDetail.as_view(), name="product-detail"),
]
