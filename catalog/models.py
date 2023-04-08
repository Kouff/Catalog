from django.db import models


class Catalog(models.Model):
    name = models.CharField(max_length=255)


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    catalog = models.ForeignKey(Catalog, models.DO_NOTHING, 'products')


class ProductParam(models.Model):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    product = models.ForeignKey(Product, models.DO_NOTHING, 'params')


class ProductImage(models.Model):
    file = models.ImageField()
    title = models.CharField(max_length=255)

    product = models.ForeignKey(Product, models.DO_NOTHING, 'images')

