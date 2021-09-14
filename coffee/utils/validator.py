import django.core.exceptions
import jsonschema

from django.core.validators import BaseValidator


class JSONSchemaValidator(BaseValidator):
    def compare(self, a, b):
        try:
            jsonschema.validate(a, b)
        except jsonschema.exceptions.ValidationError:
            raise django.core.exceptions.ValidationError("")


