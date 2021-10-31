from django.urls import path
from .views import ProductList,ProductDetail, CategoryDetail

urlpatterns = [
    path('product/',  ProductList.as_view(), name="products"),
    path('products/<slug:product_category_slug>/<slug:product_slug>/',  
          ProductDetail.as_view(), name="product-detail"),
    path('products/<slug:product_category_slug>/' , CategoryDetail.as_view()),
]
