from customeraccess.models import Receiver
import django_filters
from .models import *


class ReceiverFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    account_no = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Receiver
        fields = ('first_name', 'account_no','country')


        


# class DebtFilter(django_filters.FilterSet):
#     sender_agent = MoneyUser.objects.filter( user_type='agent')
#     sender_cu = MoneyUser.objects.filter( user_type='customer',)
#     outstanding_amount = django_filters.NumberFilter(lookup_expr='icontains')

#     class Meta:
#         model = MoneyTransfer
#         fields = ('sender_agent', 'sender_cu','outstanding_amount')

        

