from django.db.models.signals import pre_save
from django.conf import settings
from coffee.utils.email import send_email_async

from .models import Order


def change_status(instance, **kwargs):
    if instance.id is not None:
        if instance.status != Order.objects.get(id=instance.id).status:
            send_email_async.delay(
                "Change status email", f"Order status changed to {instance.status}",
                settings.EMAIL_HOST_USER, instance.email
            )
        if instance.status == Order.STATUS_DELIVERED:
            instance.is_active = False


def cancel_order(instance, **kwargs):
    if instance.id is not None:
        if not instance.is_active:
            send_email_async.delay("Cancel Order", f"Order {instance.id} is canceled", settings.EMAIL_HOST_USER, instance.email)


pre_save.connect(change_status, Order)
pre_save.connect(cancel_order, Order)
