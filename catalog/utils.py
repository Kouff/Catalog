from django.db.models import Count

from catalog.models import ProductParam


def get_params_from_products(queryset):
    params = {}

    for param_data in ProductParam.objects \
            .filter(product_id__in=queryset.values_list('id').distinct()) \
            .values('name', 'value') \
            .annotate(count=Count('product_id', distinct=True)):
        param = params.setdefault(param_data.pop('name'), list())
        param.append(param_data)

    return [{'name': param, 'values': values} for param, values in params.items()]
