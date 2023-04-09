from django.urls import path

from catalog.views import CatalogListAPIView, ProductListAPIView, ProductDetailAPIView

urlpatterns = [
    path('catalogs/', CatalogListAPIView.as_view()),
    path('catalogs/<int:catalog_id>/products/', ProductListAPIView.as_view()),
    path('products/<int:pk>/', ProductDetailAPIView.as_view()),
]
