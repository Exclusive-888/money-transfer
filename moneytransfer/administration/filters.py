
import django_filters
from django_filters import CharFilter

from .models import *


class AgentFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    username = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = MoneyUser
        fields = ('username', 'first_name','country')
        


class CustomerFilter(django_filters.FilterSet):
    username = CharFilter(field_name='username', lookup_expr='icontains')

    class Meta:
        model = MoneyUser
        fields = ('username', 'nationality','country')


class AgentBankFilter(django_filters.FilterSet):
    bank_name = django_filters.CharFilter(lookup_expr='icontains')
    account_name = django_filters.CharFilter(lookup_expr='icontains')
    account_no = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = BankUser
        fields = ('bank_name', 'account_name','account_no')


class CustomerBankFilter(django_filters.FilterSet):
    bank_name = django_filters.CharFilter(lookup_expr='icontains')
    account_name = django_filters.CharFilter(lookup_expr='icontains')
    account_no = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = BankUser
        fields = ('bank_name', 'account_name','account_no')


class CurrencyFilter(django_filters.FilterSet):
    market_rate = django_filters.NumberFilter(lookup_expr='icontains')
    total_commission = django_filters.NumberFilter(lookup_expr='icontains')


    class Meta:
        model = CurrencyRate
        fields = ('from_currency', 'to_currency','market_rate', 'total_commission')


class ReasonFilter(django_filters.FilterSet):
    reason_type = django_filters.CharFilter(lookup_expr='icontains')


    class Meta:
        model = ReasonType
        fields = ('reason_type',)


class FaqFilter(django_filters.FilterSet):
    faq_question = django_filters.CharFilter(lookup_expr='icontains')


    class Meta:
        model = Faq
        fields = ('faq_question',)
