from administration.models import CurrencyRate, ReasonType
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
from django.dispatch import receiver
import random


# Create your models here.
"**************************************RECEIVER MODEL************************************"   
def generate_pk():
    number = random.randint(1000, 9999)
    return 'CUTRN{}{}'.format(random.randint(10,55), number)

class Receiver(models.Model):
    TITLE = (
    ('mr', 'Mr.'), 
    ('mrs', 'Mrs.'),
    ('ms', 'Ms.'),
    ('miss', 'Miss.'),
    ('dr', 'Dr.'),
    )
    title_type = models.CharField(choices=TITLE, max_length=30, null=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=70, null=True)
    email = models.EmailField(unique=True)
    mobile_no = PhoneNumberField(null=True)
    city = models.CharField(max_length=50, null=True)
    country = CountryField()
    account_name = models.CharField(max_length=100, null=True)
    account_no = models.CharField(max_length=100, null=True)
    branch_code = models.CharField(max_length=70, null=True)
    bank_name = models.CharField(max_length=70, null=True)
    bank_contact = PhoneNumberField(null=True, blank=True)
    bank_email = models.EmailField(unique=False,null=True, blank=True)
    description = models.CharField(max_length=150, blank=True)

    def __str__(self):
	    return self.email 

       

"**************************************SEND-MONEY MODEL************************************"   
class SendMoney(models.Model):
    receiver = models.ForeignKey(Receiver, null=True, on_delete=models.CASCADE)
    CURRENCY = (('AED', 'AED'),('ARS', 'ARS'),('AUD', 'AUD'),('BGN', 'BGN'),('BRL', 'BRL'),('BSD', 'BSD'),('CAD', 'CAD'),('CHF', 'CHF'),('CLP', 'CLP'),('CNY', 'CNY'),('COP', 'COP'),('CZK', 'CZK'),('DKK', 'DKK'),('DOP', 'DOP'),('EGP', 'EGP'),('EUR', 'EUR'),('FJD', 'FJD'),('GBP', 'GBP'),('GTQ', 'GTQ'),('HKD', 'HKD'),('HRK', 'HRK'),('HUF', 'HUF'),('IDR', 'IDR'),('ILS', 'ILS'),('INR', 'INR'),('ISK', 'ISK'),('JPY', 'JPY'),('KRW', 'KRW'),('KZT', 'KZT'),('MXN', 'MXN'),('MYR', 'MYR'),('NOK', 'NOK'),('NZD', 'NZD'),('PAB', 'PAB'),('PEN', 'PEN'),('PHP', 'PHP'),('PKR', 'PKR'),('PLN', 'PLN'),('PYG', 'PYG'),('RON', 'RON'),('RUB', 'RUB'),('SAR', 'SAR'),('SEK', 'SEK'),('SAR', 'SAR'),('SGD', 'SGD'),('THB', 'THB'),('TRY', 'TRY'),('TWD', 'TWD'),('UAH', 'UAH'),('USD', 'USD'),('UYU', 'UYU'),('VND', 'VND'),('ZAR', 'ZAR'))
    from_currency = models.CharField(choices=CURRENCY, max_length=5, null=True, blank=True)
    to_currency = models.CharField(choices=CURRENCY, max_length=5, null=True, blank=True)
    our_rate = models.DecimalField(max_digits=15, decimal_places=2)
    send_amount = models.DecimalField(max_digits=15, decimal_places=2) 
    total_amount = models.DecimalField(max_digits=20, null=True, decimal_places=2)
    sending_money = (
        ('bank', 'Bank Transfer'), 
        ('cash', 'Cash Transfer'),
        ('cheque', 'Cheque Transfer'),
        )
    send_method = models.CharField(choices=sending_money, max_length=30, null=True)
    transfer_rate = models.DecimalField(max_digits=20, null=True, decimal_places=2)
    receive_amount = models.DecimalField(max_digits=20, null=True, decimal_places=2)
    account_name = models.CharField(max_length=100, null=True)
    account_no = models.CharField(max_length=100, null=True)
    branch_code = models.CharField(max_length=70, null=True)
    bank_name = models.CharField(max_length=70, null=True)
    bank_contact = PhoneNumberField(null=True, blank=True)
    bank_email = models.EmailField(unique=False,null=True, blank=True)
    receive_method = models.CharField(choices=sending_money, max_length=30, null=True)
    reason_type = models.ForeignKey(ReasonType, null=True, on_delete=models.SET_NULL)
    transaction_id = models.CharField(max_length = 20, default = generate_pk, editable=False)
    trans_status = (
        ('Sent', 'Sent'), 
        ('Ready To Collect', 'Ready To Collect'),
        ('Received', 'Received'),
        ('Cancelled', 'Cancelled'),
        )
    money_status = models.CharField(choices=trans_status, max_length=30, blank=True, default='Sent')
    transaction_date = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=150, blank=True)


    def save(self, *args, **kwargs):
      super().save(*args, **kwargs)
      if not self.transaction_id:            
         self.transaction_id = generate_pk   
         self.save()                                  
    

    def __str__(self):
        return str(self.transaction_id)
    













    

