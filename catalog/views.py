from rest_framework.generics import ListAPIView

from catalog.filters import ProductParamsFilterBackend
from catalog.models import Catalog, Product
from catalog.serializers import CatalogSerializer, ProductSerializer


class CatalogListAPIView(ListAPIView):
    model = Catalog
    serializer_class = CatalogSerializer
    queryset = Catalog.objects.all()


class ProductListAPIView(ListAPIView):
    model = Product
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = (ProductParamsFilterBackend,)

    def get_queryset(self):
        catalog_id = self.kwargs['catalog_id']
        return self.queryset.filter(catalog_id=catalog_id)
