from django.contrib import admin
from administration.models import MoneyUser, Agent, Customer, CurrencyRate, ReasonType, BankUser, Faq

# Register your models here.
admin.site.register(MoneyUser)
admin.site.register(Agent)
admin.site.register(CurrencyRate)
admin.site.register(ReasonType)
admin.site.register(BankUser)
admin.site.register(Customer)
admin.site.register(Faq)

