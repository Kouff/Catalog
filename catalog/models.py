from django.db import models


class Catalog(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    catalog = models.ForeignKey(Catalog, models.DO_NOTHING, 'products')

    def __str__(self):
        return self.name

    class Meta:
        indexes = (
            models.Index(fields=('catalog',)),
        )


class ProductParam(models.Model):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    product = models.ForeignKey(Product, models.DO_NOTHING, 'params')

    class Meta:
        indexes = (
            models.Index(fields=('name', 'value')),
            models.Index(fields=('product',)),
        )


class ProductImage(models.Model):
    file = models.ImageField(upload_to='products')
    title = models.CharField(max_length=255)

    product = models.ForeignKey(Product, models.DO_NOTHING, 'images')

    class Meta:
        indexes = (
            models.Index(fields=('product',)),
        )
