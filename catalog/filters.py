import operator
from functools import reduce

from django.db.models import F
from django.db.models.functions import Lower
from rest_framework.filters import BaseFilterBackend


class ProductParamsFilterBackend(BaseFilterBackend):

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

    def filter_queryset(self, request, queryset, view):
        params = request.query_params

        if params:
            querysets = self.make_querysets(params, queryset)
            return self.make_intersection_queryset(querysets)

        return queryset
