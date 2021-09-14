from rest_framework.exceptions import APIException
from django.utils.translation import ugettext_lazy as _


class OptionException(APIException):
    status_code = 400
    default_detail = _("Options are not valid, please choose valid options")
    default_code = "invalid_chosen_options"

class InvalidOrderStatusForCancel(APIException):
    status_code = 400
    default_detail = _("You can just cancel order in waiting status")
    default_code = "invalid_status_for_cancel_order"
