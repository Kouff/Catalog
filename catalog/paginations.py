from collections import OrderedDict

from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from catalog.utils import get_params_from_products


class ProductParamsOffsetPagination(LimitOffsetPagination):
    params = None

    @staticmethod
    def get_params(queryset):
        return get_params_from_products(queryset)

    def paginate_queryset(self, queryset, request, view=None):
        self.params = self.get_params(queryset)
        return super().paginate_queryset(queryset, request, view)

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data),
            ('params', self.params),
        ]))
