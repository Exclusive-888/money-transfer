from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from customeraccess.models import SendMoney, Receiver
# Register your models here.

class SendAdmin(admin.ModelAdmin):
    list_display = ("receiver", "total_amount", "id", "transaction_date", "transaction_id")


class ReceiverAdmin(admin.ModelAdmin):
    list_display = ("email", "first_name", "country")


admin.site.register(SendMoney, SendAdmin)
admin.site.register(Receiver, ReceiverAdmin)


