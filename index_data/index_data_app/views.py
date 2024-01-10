
from rest_framework.pagination import PageNumberPagination
from django.core.paginator import Paginator
from django.db import models
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import NiftyNext50, NiftySmallcap50, NiftyMidcap50, NiftyMidcap150, Nifty50
from .serializers import (
    Nifty50Serializer,
    NiftyNext50Serializer,
    NiftyMidcap50Serializer,
    NiftySmallcap50Serializer,
    NiftyMidcap150Serializer,
)

class BaseFilter(APIView):
    model = None
    serializer_class = None
    pagination_class = None

    def apply_filter(self, queryset, param, field_name, operator):
        value = self.request.query_params.get(param)
        if value:
            filter_kwargs = {f'{field_name}__{operator}': float(value)}
            queryset = queryset.filter(**filter_kwargs)
        return queryset
    def get_queryset(self):
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')

        queryset = NiftyMidcap150.objects.filter(date__range=[start_date, end_date])

        queryset = self.apply_filter(queryset, 'open_above', 'open', 'gt')
        queryset = self.apply_filter(queryset, 'closed_above', 'close', 'gt')
        queryset = self.apply_filter(queryset, 'open_above', 'open', 'gt')
        queryset = self.apply_filter(queryset, 'closed_above', 'close', 'gt')
        queryset = self.apply_filter(queryset, 'open_below', 'open', 'lt')
        queryset = self.apply_filter(queryset, 'closed_below', 'close', 'lt')
        queryset = self.apply_filter(queryset, 'high_above', 'high', 'gt')
        queryset = self.apply_filter(queryset, 'high_below', 'high', 'lt')
        queryset = self.apply_filter(queryset, 'low_above', 'low', 'gt')
        queryset = self.apply_filter(queryset, 'low_below', 'low', 'lt')
        queryset = self.apply_filter(queryset, 'turnover_greater_than', 'turnover', 'gt')
        queryset = self.apply_filter(queryset, 'turnover_less_than', 'turnover', 'lt')
        queryset = self.apply_filter(queryset, 'shares_traded_greater_than', 'shares_traded', 'gt')
        queryset = self.apply_filter(queryset, 'shares_traded_less_than', 'shares_traded', 'lt')

        return queryset

    def get_ranges(self, queryset):
        ranges = {
            'open': {
                'lowest': queryset.aggregate(lowest_open=models.Min('open'))['lowest_open'],
                'highest': queryset.aggregate(highest_open=models.Max('open'))['highest_open'],
            },
            'close': {
                'lowest': queryset.aggregate(lowest_close=models.Min('close'))['lowest_close'],
                'highest': queryset.aggregate(highest_close=models.Max('close'))['highest_close'],
            },
            'shares_traded': {
                'lowest': queryset.aggregate(lowest_shares_traded=models.Min('shares_traded'))['lowest_shares_traded'],
                'highest': queryset.aggregate(highest_shares_traded=models.Max('shares_traded'))[
                    'highest_shares_traded'],
            },
            # Add other fields for ranges
        }
        return ranges

    def get_response_data(self, queryset, data, ranges):
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')

        response_data = {
            'start-date': start_date,
            'end-date': end_date,
            'data': data,
            'ranges': ranges,
        }
        return response_data

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        # Apply pagination
        if self.pagination_class:
            page = self.request.query_params.get('page', 1)
            paginator = Paginator(queryset, 25)
            paginated_queryset = paginator.page(page)
            data = self.serializer_class(paginated_queryset, many=True).data
        else:
            data = self.serializer_class(queryset, many=True).data

        ranges = self.get_ranges(queryset)
        response_data = self.get_response_data(queryset, data, ranges)

        return Response(response_data)


class Nifty50Filter(BaseFilter):
    model = Nifty50
    serializer_class = Nifty50Serializer
    pagination_class = PageNumberPagination


class NiftyNext50Filter(BaseFilter):
    model = NiftyNext50
    serializer_class = NiftyNext50Serializer
    pagination_class = PageNumberPagination


class NiftySmallcap50Filter(BaseFilter):
    model = NiftySmallcap50
    serializer_class = NiftySmallcap50Serializer
    pagination_class = PageNumberPagination


class NiftyMidcap50Filter(BaseFilter):
    model = NiftyMidcap50
    serializer_class = NiftyMidcap50Serializer
    pagination_class = PageNumberPagination


class NiftyMidcap150Filter(BaseFilter):
    model = NiftyMidcap150
    serializer_class = NiftyMidcap150Serializer
    pagination_class = PageNumberPagination
