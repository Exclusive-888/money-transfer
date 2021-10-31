from typing import Type
from administration.models import Agent, BankUser, CurrencyRate, Customer, MoneyUser, ReasonType
from django.db import models
import random
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

# Create your models here.
def generate_pk():
    number = random.randint(1000, 9999)
    return 'MTRN{}{}'.format(random.randint(10,55), number)

class MoneyTransfer(models.Model):
    sender_agent = models.ForeignKey(MoneyUser, null=True, on_delete=models.SET_NULL, related_name='sender_agent')
    receiver_agent = models.ForeignKey(MoneyUser, null=True, on_delete=models.SET_NULL, related_name='receiver_agent')
    sending_date = models.DateField(auto_now_add=True)
    sender_cu = models.ForeignKey(MoneyUser, null=True, on_delete=models.SET_NULL, related_name='sender_cu')
    receiver_cu = models.ForeignKey(MoneyUser, null=True, on_delete=models.SET_NULL, related_name='receiver_cu')
    sending_money = (
        ('bank', 'Bank Transfer'), 
        ('cash', 'Cash Transfer'),
        ('cheque', 'Cheque Transfer'),
        ('debt', 'Debt'),
        )
    send_method = models.CharField(choices=sending_money, max_length=30, null=True)
    receiving_money = (
        ('bank', 'Bank Transfer'), 
        ('cash', 'Cash Transfer'),
        ('cheque', 'Cheque Transfer'),
        )
    receive_method = models.CharField(choices=receiving_money, max_length=30, null=True) 
    agent_bank = models.ForeignKey(BankUser, null=True, on_delete=models.SET_NULL, blank=True)
    CURRENCY = (('AED', 'AED'),('ARS', 'ARS'),('AUD', 'AUD'),('BGN', 'BGN'),('BRL', 'BRL'),('BSD', 'BSD'),('CAD', 'CAD'),('CHF', 'CHF'),('CLP', 'CLP'),('CNY', 'CNY'),('COP', 'COP'),('CZK', 'CZK'),('DKK', 'DKK'),('DOP', 'DOP'),('EGP', 'EGP'),('EUR', 'EUR'),('FJD', 'FJD'),('GBP', 'GBP'),('GTQ', 'GTQ'),('HKD', 'HKD'),('HRK', 'HRK'),('HUF', 'HUF'),('IDR', 'IDR'),('ILS', 'ILS'),('INR', 'INR'),('ISK', 'ISK'),('JPY', 'JPY'),('KRW', 'KRW'),('KZT', 'KZT'),('MXN', 'MXN'),('MYR', 'MYR'),('NOK', 'NOK'),('NZD', 'NZD'),('PAB', 'PAB'),('PEN', 'PEN'),('PHP', 'PHP'),('PKR', 'PKR'),('PLN', 'PLN'),('PYG', 'PYG'),('RON', 'RON'),('RUB', 'RUB'),('SAR', 'SAR'),('SEK', 'SEK'),('SAR', 'SAR'),('SGD', 'SGD'),('THB', 'THB'),('TRY', 'TRY'),('TWD', 'TWD'),('UAH', 'UAH'),('USD', 'USD'),('UYU', 'UYU'),('VND', 'VND'),('ZAR', 'ZAR'))
    from_currency = models.CharField(choices=CURRENCY, max_length=5, null=True)
    to_currency = models.CharField(choices=CURRENCY, max_length=5, null=True)
    total_commission = models.ForeignKey(CurrencyRate, null=True, on_delete=models.SET_NULL, related_name='total_commission2')
    transfer_rate = models.DecimalField(max_digits=20, null=True, decimal_places=2)
    transaction_id = models.CharField(max_length = 20, default = generate_pk, editable=False)
    sending_amount = models.DecimalField(max_digits=20, null=True, decimal_places=2) 
    receiving_amount = models.DecimalField(max_digits=20, null=True, decimal_places=2)
    paid_amount = models.DecimalField(max_digits=20, null=True, decimal_places=2, blank=True)
    due_date = models.DateField(null=True, blank=True)
    outstanding_amount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    total_payment = models.DecimalField(max_digits=20, null=True, decimal_places=2)
    pay_status = (
        ('sent', 'Sent'), 
        ('processing', 'Processing'), 
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
        )
    payment_status = models.CharField(choices=pay_status, max_length=30, null=True, default='Sent')
    reason_type = models.ForeignKey(ReasonType, null=True, on_delete=models.SET_NULL)
    notify = (
        ('sms', 'Sms'), 
        ('email', 'Email'),
        ('both', 'Both'),
        )
    notification_type = models.CharField(choices=notify, max_length=30, null=True)
    notes = models.CharField(max_length=150, blank=True)

    def save(self, *args, **kwargs):
      super().save(*args, **kwargs)
      if not self.transaction_id:                                # if uid of the instance is blank
         self.transaction_id = generate_pk   # generating the uid and allocating the value
         self.save()                                   # saving the instance
          
    
    def __str__(self):
        return str(self.transaction_id)




class DebtTransfer(models.Model):
    debt_id = models.CharField(max_length = 20, null=True, blank=True)
    receiver_customer = models.ForeignKey(MoneyUser, null=True, on_delete=models.SET_NULL, related_name='receiver_customer', blank=True)
    sender_agent = models.ForeignKey(MoneyUser, null=True, on_delete=models.SET_NULL, related_name='sender_agentdb', blank=True)
    receiving_amount = models.DecimalField(max_digits=20, null=True, decimal_places=2, blank=True)
    CURRENCY = (('AED', 'AED'),('ARS', 'ARS'),('AUD', 'AUD'),('BGN', 'BGN'),('BRL', 'BRL'),('BSD', 'BSD'),('CAD', 'CAD'),('CHF', 'CHF'),('CLP', 'CLP'),('CNY', 'CNY'),('COP', 'COP'),('CZK', 'CZK'),('DKK', 'DKK'),('DOP', 'DOP'),('EGP', 'EGP'),('EUR', 'EUR'),('FJD', 'FJD'),('GBP', 'GBP'),('GTQ', 'GTQ'),('HKD', 'HKD'),('HRK', 'HRK'),('HUF', 'HUF'),('IDR', 'IDR'),('ILS', 'ILS'),('INR', 'INR'),('ISK', 'ISK'),('JPY', 'JPY'),('KRW', 'KRW'),('KZT', 'KZT'),('MXN', 'MXN'),('MYR', 'MYR'),('NOK', 'NOK'),('NZD', 'NZD'),('PAB', 'PAB'),('PEN', 'PEN'),('PHP', 'PHP'),('PKR', 'PKR'),('PLN', 'PLN'),('PYG', 'PYG'),('RON', 'RON'),('RUB', 'RUB'),('SAR', 'SAR'),('SEK', 'SEK'),('SAR', 'SAR'),('SGD', 'SGD'),('THB', 'THB'),('TRY', 'TRY'),('TWD', 'TWD'),('UAH', 'UAH'),('USD', 'USD'),('UYU', 'UYU'),('VND', 'VND'),('ZAR', 'ZAR'))
    from_currency = models.CharField(choices=CURRENCY, max_length=5, null=True, blank=True)
    to_currency = models.CharField(choices=CURRENCY, max_length=5, null=True, blank=True)
    total_commission = models.ForeignKey(CurrencyRate, null=True, on_delete=models.SET_NULL, related_name='total_commission1', blank=True)
    sending_amount = models.DecimalField(max_digits=20, null=True, decimal_places=2) 
    receiving_amount = models.DecimalField(max_digits=20, null=True, decimal_places=2)
    paid_amount = models.DecimalField(max_digits=20, null=True, decimal_places=2, blank=True)
    due_date = models.DateField(null=True, blank=True)
    outstanding_amount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    sending_money = (
        ('bank', 'Bank Transfer'), 
        ('cash', 'Cash Transfer'),
        ('cheque', 'Cheque Transfer'),
        ('debt', 'Debt'),
        )
    debt = models.CharField(choices=sending_money, max_length=30, null=True, blank=True)

    def __str__(self):
        return str(self.outstanding_amount)


@receiver(post_save, sender=MoneyTransfer)
def create_debt(sender, instance, created, **kwargs):
    if created:
      if instance.receiver_cu or instance.sender_agent or instance.receiving_amount or instance.paid_amount or instance.due_date or instance.outstanding_amount or instance.from_currency or instance.to_currency or instance.total_commission or instance.send_method == 'debt' or instance.transaction_id or instance.sending_amount:
         DebtTransfer.objects.create(receiver_customer = instance.receiver_cu, sender_agent = instance.sender_agent, 
         receiving_amount = instance.receiving_amount, paid_amount = instance.paid_amount, outstanding_amount = instance.outstanding_amount, 
         due_date = instance.due_date, from_currency = instance.from_currency, to_currency = instance.to_currency, 
         total_commission = instance.total_commission, debt = instance.send_method, debt_id = instance.transaction_id, 
         sending_amount = instance.sending_amount,)





