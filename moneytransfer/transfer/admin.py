from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from transfer.models import MoneyTransfer, DebtTransfer

# Register your models here.
class TransferAdmin(admin.ModelAdmin):
    list_display = ("sender_agent", "sender_cu", "from_currency", "total_payment", "payment_status", "transaction_id")


admin.site.register(MoneyTransfer, TransferAdmin)
admin.site.register(DebtTransfer)

