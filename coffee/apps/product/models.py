from django.db import models
from django.utils.translation import ugettext as _
from django_better_admin_arrayfield.models.fields import ArrayField

OPTION_JSON_SCHEMA = {
    "type": "object",
    "properties": {
        "title": {"type": "string"},
        "choices": {"type": "array"},
    }
}


class Option(models.Model):
    title = models.CharField(_("Title"), max_length=32, null=False, blank=False)
    choices = ArrayField(
        base_field=models.CharField(verbose_name=_("Choices"), max_length=32), null=False
    )

    class Meta:
        verbose_name = _("Option")
        verbose_name_plural = _("Options")

    def __str__(self):
        return "{0}  ({1})".format(self.title, ','.join(self.choices))


PRODUCT_JSON_SCHEMA = {
    "type": "object",
    "properties": {
        "pk": {"type": "number"},
        "title": {"type": "string"},
        "price": {"type": "number"},
        "options": {"type": "array", "items": OPTION_JSON_SCHEMA}
    },
}


class Product(models.Model):
    title = models.CharField(verbose_name=_("Title"), max_length=32, null=False, blank=False)
    price = models.FloatField(verbose_name=_("Price"), null=False, blank=False)
    options = models.ManyToManyField(verbose_name=_("Options"), related_name='products', to=Option)
    created_date = models.DateTimeField(verbose_name=_("Create Date"), auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name=_("Update Date"), auto_now=True)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.title
