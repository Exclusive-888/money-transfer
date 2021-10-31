from administration.models import MoneyUser
import django_filters
from .models import *


class MoneyFilter(django_filters.FilterSet):
    sender_agent = MoneyUser.objects.filter( user_type='agent')
    sender_cu = MoneyUser.objects.filter( user_type='customer',)
    total_payment = django_filters.NumberFilter(lookup_expr='icontains')

    class Meta:
        model = MoneyTransfer
        fields = ('sender_agent', 'sender_cu','total_payment')


        


class DebtFilter(django_filters.FilterSet):
    sender_agent = MoneyUser.objects.filter( user_type='agent')
    sender_cu = MoneyUser.objects.filter( user_type='customer',)
    outstanding_amount = django_filters.NumberFilter(lookup_expr='icontains')

    class Meta:
        model = MoneyTransfer
        fields = ('sender_agent', 'sender_cu','outstanding_amount')

        

