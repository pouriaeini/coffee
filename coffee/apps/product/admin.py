from django.contrib import admin
from .models import Product, Option
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin


class ProductAdmin(admin.ModelAdmin):
    pass


class OptionAdmin(admin.ModelAdmin, DynamicArrayMixin):
    pass


admin.site.register(Product, ProductAdmin)
admin.site.register(Option, OptionAdmin)
