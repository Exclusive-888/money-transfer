from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from exchange.models import MoneyExchange

# Register your models here.
class ExchangeAdmin(admin.ModelAdmin):
    list_display = ("buying_currency", "selling_currency", "buying_amount", "exchange_date", "exchange_id")


admin.site.register(MoneyExchange, ExchangeAdmin)
