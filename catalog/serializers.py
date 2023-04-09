from rest_framework import serializers

from catalog.models import Catalog, Product, ProductParam, ProductImage


class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = ('id', 'name')


class ProductListSerializer(serializers.ModelSerializer):
    price = serializers.FloatField()

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price')


class ProductParamSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductParam
        fields = ('name', 'value')


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('file', 'title')


class ProductDetailSerializer(serializers.ModelSerializer):
    price = serializers.FloatField()
    images = ProductImageSerializer(many=True)
    params = ProductParamSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'images', 'params')
