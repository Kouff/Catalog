from rest_framework.generics import ListAPIView, RetrieveAPIView

from catalog.filters import ProductParamsFilterBackend
from catalog.models import Catalog, Product
from catalog.paginations import ProductParamsOffsetPagination
from catalog.serializers import CatalogSerializer, ProductListSerializer, ProductDetailSerializer


class CatalogListAPIView(ListAPIView):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    filter_backends = (ProductParamsFilterBackend,)
    pagination_class = ProductParamsOffsetPagination

    def get_queryset(self):
        catalog_id = self.kwargs['catalog_id']
        return self.queryset.filter(catalog_id=catalog_id)


class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.prefetch_related('params', 'images').all()
    serializer_class = ProductDetailSerializer
