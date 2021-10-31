from django.db.models.signals import post_delete, post_save, pre_save, pre_delete
from django.dispatch import receiver
from administration.models import MoneyUser

"**************************************USERNAME CREATE************************************" 

@receiver(pre_save, sender=MoneyUser)
def username_create(sender ,instance, **kwargs):
    if not instance.username:
        instance.username = instance.email

pre_save.connect(username_create, sender = MoneyUser)
