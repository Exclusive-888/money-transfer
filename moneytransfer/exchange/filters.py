import django_filters
from .models import *


class ExchangeFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    selling_amount = django_filters.NumberFilter(lookup_expr='icontains')
    buying_amount = django_filters.NumberFilter(lookup_expr='icontains')

    class Meta:
        model = MoneyExchange
        fields = ('first_name', 'selling_amount','buying_amount')


        


