from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class OrderConfig(AppConfig):
    name = 'coffee.apps.order'
    verbose_name = _("Order")

    def ready(self):
        import coffee.apps.order.signal
