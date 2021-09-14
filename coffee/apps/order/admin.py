from django.contrib import admin

from .models import Order


class OrderAdmin(admin.ModelAdmin):
    exclude = ['order_detail', ]


admin.site.register(Order, OrderAdmin)
