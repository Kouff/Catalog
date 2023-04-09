from django.contrib import admin

from catalog.models import Catalog, Product, ProductParam, ProductImage

admin.site.register(Catalog)


class ProductParamInline(admin.StackedInline):
    model = ProductParam
    extra = 1
    extra_to_create = 6

    def get_extra(self, request, obj=None, **kwargs):
        return self.extra_to_create if obj is None else self.extra


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductImageInline,
        ProductParamInline,
    ]
