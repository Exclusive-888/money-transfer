from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from administration.models import  Agent, CurrencyRate, Customer
from django.db import models
import random

# Create your models here.
def generate_pk():
    number = random.randint(1000, 9999)
    return 'MEXTN{}{}'.format(random.randint(10,55), number)


class MoneyExchange(models.Model):
    exchange_id = models.CharField(max_length = 20, default = generate_pk, editable=False)
    CURRENCY = (('AED', 'AED'),('ARS', 'ARS'),('AUD', 'AUD'),('BGN', 'BGN'),('BRL', 'BRL'),('BSD', 'BSD'),('CAD', 'CAD'),('CHF', 'CHF'),('CLP', 'CLP'),('CNY', 'CNY'),('COP', 'COP'),('CZK', 'CZK'),('DKK', 'DKK'),('DOP', 'DOP'),('EGP', 'EGP'),('EUR', 'EUR'),('FJD', 'FJD'),('GBP', 'GBP'),('GTQ', 'GTQ'),('HKD', 'HKD'),('HRK', 'HRK'),('HUF', 'HUF'),('IDR', 'IDR'),('ILS', 'ILS'),('INR', 'INR'),('ISK', 'ISK'),('JPY', 'JPY'),('KRW', 'KRW'),('KZT', 'KZT'),('MXN', 'MXN'),('MYR', 'MYR'),('NOK', 'NOK'),('NZD', 'NZD'),('PAB', 'PAB'),('PEN', 'PEN'),('PHP', 'PHP'),('PKR', 'PKR'),('PLN', 'PLN'),('PYG', 'PYG'),('RON', 'RON'),('RUB', 'RUB'),('SAR', 'SAR'),('SEK', 'SEK'),('SAR', 'SAR'),('SGD', 'SGD'),('THB', 'THB'),('TRY', 'TRY'),('TWD', 'TWD'),('UAH', 'UAH'),('USD', 'USD'),('UYU', 'UYU'),('VND', 'VND'),('ZAR', 'ZAR'))
    buying_currency = models.CharField(choices=CURRENCY, max_length=5, null=True, blank=True)
    selling_currency = models.CharField(choices=CURRENCY, max_length=5, null=True, blank=True)
    buying_amount = models.DecimalField(max_digits=15, decimal_places=2) 
    selling_amount = models.DecimalField(max_digits=12, decimal_places=2) 
    exchange_rate = models.ForeignKey(CurrencyRate, null=True, on_delete=models.SET_NULL, related_name='money_exchange_rate')
    exchange_date = models.DateTimeField(auto_now_add=True)
    assign_agent = models.ForeignKey(Agent, null=True, on_delete=models.SET_NULL)
    customer_info = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL, related_name='customer_info', blank=True)
    customer_name = models.CharField(max_length=100, null=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    mobile_no = PhoneNumberField()
    address = models.CharField(max_length=150, null=True)
    city = models.CharField(max_length=10, null=True)
    postal_code = models.CharField(max_length=10, null=True, blank=True)
    state = models.CharField(max_length=20, null=True, blank=True)
    photo_id = models.CharField(max_length=80, null=True)
    country = CountryField()

    def save(self, *args, **kwargs):
      super().save(*args, **kwargs)
      if not self.exchange_id:                                # if uid of the instance is blank
         self.exchange_id = generate_pk   # generating the uid and allocating the value
         self.save()                                   # saving the instance
          
    
    def __str__(self):
        return str(self.exchange_id)

