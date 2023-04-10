import operator
from functools import reduce

from django.db.models import F
from django.db.models.functions import Lower
from rest_framework.filters import BaseFilterBackend


class ProductParamsFilterBackend(BaseFilterBackend):
    except_query_params = ('limit', 'offset')

    @staticmethod
    def make_querysets(params, queryset):
        queryset = queryset.annotate(pname=F('params__name'), pvalue=Lower('params__value'))
        querysets = []
        for name in params:
            values = [value.lower() for value in params.getlist(name)]
            querysets.append(queryset.filter(pname__iexact=name, pvalue__in=values).distinct('id'))
        return querysets

    @staticmethod
    def make_intersection_queryset(querysets):
        return reduce(operator.and_, querysets)

    def get_query_params(self, request):
        params = request.query_params.copy()

        for except_query_param in self.except_query_params:
            params.pop(except_query_param, None)

        return params

    def filter_queryset(self, request, queryset, view):
        params = self.get_query_params(request)

        if params:
            querysets = self.make_querysets(params, queryset)
            return self.make_intersection_queryset(querysets)

        return queryset
