from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
from decimal import Decimal
from django.db.models.signals import post_delete, post_save, pre_save, pre_delete
from django.dispatch import receiver




"**************************************User-Model*********************************"
class MoneyUser(AbstractUser):
    user_type_data = (
        ('superuser', 'Super Admin'),
        ('agent', 'Agent'), 
        ('customer', 'Customer'),
        )
    user_type = models.CharField(choices=user_type_data, max_length=30, null=True)
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
    arabic_name = models.CharField(max_length=70, null=True, blank=True)
    mobile_no = PhoneNumberField(null=True)
    office_no = PhoneNumberField(null=True, blank=True)
    home_no = PhoneNumberField(null=True, blank=True)
    DOCUMENTS = (
        ('pass', 'Passport'), 
        ('dl', 'Driving License'),
        ('nic', 'NIC'),
        ('rp', 'Residence Permit'),
        ('other', 'Other'),
        )
    documents_type = models.CharField(choices=DOCUMENTS, max_length=50, null=True, blank=True)
    document_upload = models.FileField(upload_to='documents/', blank=True)
    document_no = models.CharField(max_length=100, null=True, blank=True)
    doc_start_date = models.DateField('Document Start Date', null=True, blank=True)
    doc_end_date = models.DateField('Document End Date', null=True, blank=True)
    prof_address = models.CharField(max_length=100, null=True, blank=True)
    notes = models.CharField(max_length=200, null=True, blank=True)
    dob = models.DateField('Date of Birth', null=True)
    address = models.CharField(max_length=100, null=True)
    postal_code = models.CharField(max_length=10, null=True, blank=True)
    city = models.CharField(max_length=50, null=True)
    country = CountryField(null=True)
    NATIONALITIES = (('Afghan', 'Afghan'), ('Albanian', 'Albanian'), ('Algerian', 'Algerian'), ('American', 'American'), ('Andorran', 'Andorran'), ('Angolan', 'Angolan'), ('Antiguans', 'Antiguans'), ('Argentinean', 'Argentinean'), ('Armenian', 'Armenian'), ('Australian', 'Australian'), ('Austrian', 'Austrian'), ('Azerbaijani', 'Azerbaijani'), ('Bahamian', 'Bahamian'), ('Bahraini', 'Bahraini'), ('Bangladeshi', 'Bangladeshi'), ('Barbadian', 'Barbadian'), ('Barbudans', 'Barbudans'), ('Batswana', 'Batswana'), ('Belarusian', 'Belarusian'), ('Belgian', 'Belgian'), ('Belizean', 'Belizean'), ('Beninese', 'Beninese'), ('Bhutanese', 'Bhutanese'), ('Bolivian', 'Bolivian'), ('Bosnian', 'Bosnian'), ('Brazilian', 'Brazilian'), ('British', 'British'), ('Bruneian', 'Bruneian'), ('Bulgarian', 'Bulgarian'), ('Burkinabe', 'Burkinabe'), ('Burmese', 'Burmese'), ('Burundian', 'Burundian'), ('Cambodian', 'Cambodian'), ('Cameroonian', 'Cameroonian'), ('Canadian', 'Canadian'), ('Cape Verdean', 'Cape Verdean'), ('Central African', 'Central African'), ('Chadian', 'Chadian'), ('Chilean', 'Chilean'), ('Chinese', 'Chinese'), ('Colombian', 'Colombian'), ('Comoran', 'Comoran'), ('Congolese', 'Congolese'), ('Costa Rican', 'Costa Rican'), ('Croatian', 'Croatian'), ('Cuban', 'Cuban'), ('Cypriot', 'Cypriot'), ('Czech', 'Czech'), ('Danish', 'Danish'), ('Djibouti', 'Djibouti'), ('Dominican', 'Dominican'), ('Dutch', 'Dutch'), ('Dutchman', 'Dutchman'), ('Dutchwoman', 'Dutchwoman'), ('East Timorese', 'East Timorese'), ('Ecuadorean', 'Ecuadorean'), ('Egyptian', 'Egyptian'), ('Emirian', 'Emirian'), ('Equatorial Guinean', 'Equatorial Guinean'), ('Eritrean', 'Eritrean'), ('Estonian', 'Estonian'), ('Ethiopian', 'Ethiopian'), ('Fijian', 'Fijian'), ('Filipino', 'Filipino'), ('Finnish', 'Finnish'), ('French', 'French'), ('Gabonese', 'Gabonese'), ('Gambian', 'Gambian'), ('Georgian', 'Georgian'), ('German', 'German'), ('Ghanaian', 'Ghanaian'), ('Greek', 'Greek'), ('Grenadian', 'Grenadian'), ('Guatemalan', 'Guatemalan'), ('Guinea-Bissauan', 'Guinea-Bissauan'), ('Guinean', 'Guinean'), ('Guyanese', 'Guyanese'), ('Haitian', 'Haitian'), ('Herzegovinian', 'Herzegovinian'), ('Honduran', 'Honduran'), ('Hungarian', 'Hungarian'), ('I-Kiribati', 'I-Kiribati'), ('Icelander', 'Icelander'), ('Indian', 'Indian'), ('Indonesian', 'Indonesian'), ('Iranian', 'Iranian'), ('Iraqi', 'Iraqi'), ('Irish', 'Irish'), ('Israeli', 'Israeli'), ('Italian', 'Italian'), ('Ivorian', 'Ivorian'), ('Jamaican', 'Jamaican'), ('Japanese', 'Japanese'), ('Jordanian', 'Jordanian'), ('Kazakhstani', 'Kazakhstani'), ('Kenyan', 'Kenyan'), ('Kittian and Nevisian', 'Kittian and Nevisian'), ('Kuwaiti', 'Kuwaiti'), ('Kyrgyz', 'Kyrgyz'), ('Laotian', 'Laotian'), ('Latvian', 'Latvian'), ('Lebanese', 'Lebanese'), ('Liberian', 'Liberian'), ('Libyan', 'Libyan'), ('Liechtensteiner', 'Liechtensteiner'), ('Lithuanian', 'Lithuanian'), ('Luxembourger', 'Luxembourger'), ('Macedonian', 'Macedonian'), ('Malagasy', 'Malagasy'), ('Malawian', 'Malawian'), ('Malaysian', 'Malaysian'), ('Maldivan', 'Maldivan'), ('Malian', 'Malian'), ('Maltese', 'Maltese'), ('Marshallese', 'Marshallese'), ('Mauritanian', 'Mauritanian'), ('Mauritian', 'Mauritian'), ('Mexican', 'Mexican'), ('Micronesian', 'Micronesian'), ('Moldovan', 'Moldovan'), ('Monacan', 'Monacan'), ('Mongolian', 'Mongolian'), ('Moroccan', 'Moroccan'), ('Mosotho', 'Mosotho'), ('Motswana', 'Motswana'), ('Mozambican', 'Mozambican'), ('Namibian', 'Namibian'), ('Nauruan', 'Nauruan'), ('Nepalese', 'Nepalese'), ('Netherlander', 'Netherlander'), ('New Zealander', 'New Zealander'), ('Ni-Vanuatu', 'Ni-Vanuatu'), ('Nicaraguan', 'Nicaraguan'), ('Nigerian', 'Nigerian'), ('Nigerien', 'Nigerien'), ('North Korean', 'North Korean'), ('Northern Irish', 'Northern Irish'), ('Norwegian', 'Norwegian'), ('Omani', 'Omani'), ('Pakistani', 'Pakistani'), ('Palauan', 'Palauan'), ('Panamanian', 'Panamanian'), ('Papua New Guinean', 'Papua New Guinean'), ('Paraguayan', 'Paraguayan'), ('Peruvian', 'Peruvian'), ('Polish', 'Polish'), ('Portuguese', 'Portuguese'), ('Qatari', 'Qatari'), ('Romanian', 'Romanian'), ('Russian', 'Russian'), ('Rwandan', 'Rwandan'), ('Saint Lucian', 'Saint Lucian'), ('Salvadoran', 'Salvadoran'), ('Samoan', 'Samoan'), ('San Marinese', 'San Marinese'), ('Sao Tomean', 'Sao Tomean'), ('Saudi', 'Saudi'), ('Scottish', 'Scottish'), ('Senegalese', 'Senegalese'), ('Serbian', 'Serbian'), ('Seychellois', 'Seychellois'), ('Sierra Leonean', 'Sierra Leonean'), ('Singaporean', 'Singaporean'), ('Slovakian', 'Slovakian'), ('Slovenian', 'Slovenian'), ('Solomon Islander', 'Solomon Islander'), ('Somali', 'Somali'), ('South African', 'South African'), ('South Korean', 'South Korean'), ('Spanish', 'Spanish'), ('Sri Lankan', 'Sri Lankan'), ('Sudanese', 'Sudanese'), ('Surinamer', 'Surinamer'), ('Swazi', 'Swazi'), ('Swedish', 'Swedish'), ('Swiss', 'Swiss'), ('Syrian', 'Syrian'), ('Taiwanese', 'Taiwanese'), ('Tajik', 'Tajik'), ('Tanzanian', 'Tanzanian'), ('Thai', 'Thai'), ('Togolese', 'Togolese'), ('Tongan', 'Tongan'), ('Trinidadian or Tobagonian', 'Trinidadian or Tobagonian'), ('Tunisian', 'Tunisian'), ('Turkish', 'Turkish'), ('Tuvaluan', 'Tuvaluan'), ('Ugandan', 'Ugandan'), ('Ukrainian', 'Ukrainian'), ('Uruguayan', 'Uruguayan'), ('Uzbekistani', 'Uzbekistani'), ('Venezuelan', 'Venezuelan'), ('Vietnamese', 'Vietnamese'), ('Welsh', 'Welsh'), ('Yemenite', 'Yemenite'), ('Zambian', 'Zambian'), ('Zimbabwean', 'Zimbabwean'))
    nationality = models.CharField(choices=NATIONALITIES, max_length=100, null=True)
    is_active = models.BooleanField(default=True, null=True)
    is_agent = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)

   
    @property
    def status(self):
        if self.is_active:
            return 'Active'
        else:
            return 'Inactive'
    
    def __str__(self):
	    return self.email


class Faq(models.Model):
    faq_question = models.CharField(max_length=300, null=True)
    faq_answer = models.CharField(max_length=1500, null=True)

    def __str__(self):
	    return self.faq_question


"**************************************USERNAME CREATE************************************" 

@receiver(pre_save, sender=MoneyUser)
def username_create(sender ,instance, **kwargs):
    if not instance.username:
        instance.username = instance.email

pre_save.connect(username_create, sender = MoneyUser)

@receiver(pre_save, sender=MoneyUser)
def create_superuser(sender ,instance, **kwargs):
    if instance.is_superuser:
        instance.user_type = 'superuser'

pre_save.connect(username_create, sender = MoneyUser)


"**************************************AGENT MODEL************************************"   
class Agent(models.Model):
    agent = models.ForeignKey(MoneyUser, null=True, on_delete=models.CASCADE)

    def __str__(self):
	    return self.agent.email 

@receiver(post_save, sender=MoneyUser)
def create_agent(sender, instance, created, **kwargs):
    if created:
      if instance.user_type == 'agent':
         Agent.objects.create(agent = instance)



@receiver(post_delete, sender=MoneyUser)
def delete_agent(sender, instance, *args, **kwargs):
    if instance.user_type == 'agent':
       instance.user_type
 
"**************************************CUSTOMER MODEL************************************"   
class Customer(models.Model):
    customer = models.ForeignKey(MoneyUser, null=True, on_delete=models.CASCADE)

    def __str__(self):
	    return self.customer.email 

@receiver(post_save, sender=MoneyUser)
def create_customer(sender, instance, created, **kwargs):
    if created:
      if instance.user_type == 'customer':
         Customer.objects.create(customer = instance)
      
@receiver(post_delete, sender=MoneyUser)
def delete_customer(sender, instance, *args, **kwargs):
    if instance.user_type == 'customer':
        instance.user_type

"**************************************CURRENCY TYPE************************************" 


class CurrencyRate(models.Model):
    CURRENCY = (('AED', 'AED'),('ARS', 'ARS'),('AUD', 'AUD'),('BGN', 'BGN'),('BRL', 'BRL'),('BSD', 'BSD'),('CAD', 'CAD'),('CHF', 'CHF'),('CLP', 'CLP'),('CNY', 'CNY'),('COP', 'COP'),('CZK', 'CZK'),('DKK', 'DKK'),('DOP', 'DOP'),('EGP', 'EGP'),('EUR', 'EUR'),('FJD', 'FJD'),('GBP', 'GBP'),('GTQ', 'GTQ'),('HKD', 'HKD'),('HRK', 'HRK'),('HUF', 'HUF'),('IDR', 'IDR'),('ILS', 'ILS'),('INR', 'INR'),('ISK', 'ISK'),('JPY', 'JPY'),('KRW', 'KRW'),('KZT', 'KZT'),('MXN', 'MXN'),('MYR', 'MYR'),('NOK', 'NOK'),('NZD', 'NZD'),('PAB', 'PAB'),('PEN', 'PEN'),('PHP', 'PHP'),('PKR', 'PKR'),('PLN', 'PLN'),('PYG', 'PYG'),('RON', 'RON'),('RUB', 'RUB'),('SAR', 'SAR'),('SEK', 'SEK'),('SAR', 'SAR'),('SGD', 'SGD'),('THB', 'THB'),('TRY', 'TRY'),('TWD', 'TWD'),('UAH', 'UAH'),('USD', 'USD'),('UYU', 'UYU'),('VND', 'VND'),('ZAR', 'ZAR'))
    from_currency = models.CharField(choices=CURRENCY, max_length=5, null=True)
    to_currency = models.CharField(choices=CURRENCY, max_length=5, null=True)
    market_rate = models.DecimalField(max_digits=8,null=True, decimal_places=2)
    our_rate = models.DecimalField(max_digits=8,null=True, decimal_places=2)
    total_commission = models.FloatField(null=True)

    
    def __str__(self):
        return str(self.total_commission)

"**************************************TRANSACTION REASON-TYPE***********************************"  

class ReasonType(models.Model):
    reason_type = models.CharField(max_length=150)

    def __str__(self):
        return self.reason_type

"**************************************BANKs***********************************"  

class BankUser(models.Model):
    bank_name = models.CharField(max_length=150)
    bank_branch_code = models.CharField(max_length=50)
    bank_address = models.CharField(max_length=200)
    bank_email = models.EmailField(null=True, blank=True)
    bank_contact = models.IntegerField(null=True, blank=True)   
    bank_type = (
        ('agentbank', 'Agent'), 
        ('customerbank', 'Customer'),
        )
    bank_user = models.CharField(choices=bank_type, max_length=30, null=True)
    bank_agent = models.ForeignKey(Agent, null=True, on_delete=models.SET_NULL)
    bank_customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    account_name = models.CharField(max_length=150, null=True)
    nick_name = models.CharField(max_length=150, null=True, blank=True)
    account_no = models.CharField(max_length=150, null=True)
    account_type = models.CharField(max_length=70, null=True)
    sort_code = models.CharField(max_length=30, null=True, blank=True)
    iban = models.CharField(max_length=70, null=True, blank=True)
    swift_code = models.CharField(max_length=80, null=True, blank=True)
    bank_country = CountryField(null=True)
    notes = models.CharField(max_length=100, blank=True)
    

    def __str__(self):
        return self.bank_name
    
"**************************************USER-TYPE SAVE************************************"   

@receiver(pre_save, sender=BankUser)
def bank_user_save(sender ,instance, **kwargs):
      if instance.bank_agent:
        instance.bank_user = 'agentbank'
      
      if instance.bank_customer:
        instance.bank_user = 'customerbank'

pre_save.connect(bank_user_save, sender = BankUser)
