from django.db import models
from django.utils.translation import ugettext as _
from django_better_admin_arrayfield.models.fields import ArrayField

from coffee.apps.product.models import Product


class Order(models.Model):
    STATUS_WAITING = "W"
    STATUS_PREPARATION = "P"
    STATUS_READY = "R"
    STATUS_DELIVERED = "D"
    STATUS_CHOICES = [
        (STATUS_WAITING, "Waiting"), (STATUS_PREPARATION, "Preparation"),
        (STATUS_READY, "Ready"), (STATUS_DELIVERED, "Delivered")
    ]
    first_name = models.CharField(verbose_name=_("First Name"), max_length=32, null=False, blank=False)
    last_name = models.CharField(verbose_name=_("Last Name"), max_length=32, null=False, blank=False)
    phone_number = models.CharField(verbose_name=_("Phone Number"), max_length=16, null=True, blank=True)
    email = models.EmailField(verbose_name=_("Email"), null=False)
    created = models.DateTimeField(verbose_name=_("Created"), auto_now=True)
    updated = models.DateTimeField(verbose_name=_("Updated"), auto_now_add=True)
    status = models.CharField(verbose_name=_("Status"), max_length=1, choices=STATUS_CHOICES, default=STATUS_WAITING)
    products = models.ManyToManyField(
        verbose_name=_("Product"), related_name="products",
        to=Product,
    )
    order_detail = ArrayField(verbose_name=_("Order Detail"), base_field=models.JSONField())
    # order_detail = models.JSONField(default=list, null=True, blank=True)
    price = models.FloatField(verbose_name=_("Price"))
    is_active = models.BooleanField(verbose_name=_("Is Active"), default=True)

    def get_fullname(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.get_fullname()

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")
