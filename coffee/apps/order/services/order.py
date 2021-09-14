from rest_framework.exceptions import ValidationError
from coffee.apps.product.services.product import ProductServices
from coffee.utils.exceptions import InvalidOrderStatusForCancel

from ..models import Order


class OrderServices:
    def __init__(self, first_name, last_name, email, phone_number, products):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.products = products
        self.product_list = []
        self.product_queryset = ProductServices.PRODUCT_OBJ_NONE_VALUE
        self.price = 0

    @classmethod
    def new_order(cls, first_name, last_name, email, phone_number, products):
        ids = [p.get("pk") for p in products]
        product_queryset = ProductServices.get_products(ids)
        price = cls.calculate_price(product_queryset, ids)
        detail = cls.create_product_list(product_queryset, products)
        order_obj = Order(
            first_name=first_name, last_name=last_name, email=email,
            phone_number=phone_number, price=price, order_detail=detail
        )
        order_obj.save()
        for p in product_queryset:
            order_obj.products.add(p)
        return order_obj

    @staticmethod
    def create_product_list(queryset, products):
        product_list = []
        for product in products:
            product_list.append(
                {
                    "title": queryset.get(id=product.get('pk')).title,
                    "option": product.get('option')
                }
            )
        return product_list

    @staticmethod
    def calculate_price(queryset, ids):
        price = 0
        for id in ids:
            price += queryset.get(id=id).price
        return price

    @staticmethod
    def get_all_active_orders():
        return Order.objects.filter(is_active=True)

    @staticmethod
    def get_order_by_id(id):
        try:
            return Order.objects.filter(id=id, is_active=True)
        except Order.DoesNotExist:
            return Order.objects.none()

    @staticmethod
    def is_waiting(queryset):
        return queryset.status == Order.STATUS_WAITING

    @classmethod
    def cancel_order(cls, id):
        order = cls.get_order_by_id(id)
        if not order.exists():
            raise ValidationError("Order is not exist")
        order = order.first()
        if cls.is_waiting(order):
            raise InvalidOrderStatusForCancel
        order.is_active = False
        order.save()

    @classmethod
    def update_order(cls, pk, *args, **kwargs):
        order = cls.get_order_by_id(pk)
        if not order.exists():
            raise ValidationError("Order is not exist")
        order = order.first()
        if not cls.is_waiting(order):
            raise InvalidOrderStatusForCancel
        order.products.clear()
        product_set = []
        for k, v in kwargs.items():
            if k == "products":
                product_set = [p.get('pk') for p in v]
                product_queryset = ProductServices.get_products(product_set)
                detail = cls.create_product_list(product_queryset, v)
                setattr(order, 'order_detail', detail)
                setattr(order, 'price', cls.calculate_price(product_queryset, product_set))
            elif hasattr(order, k):
                setattr(order, k, v)

        order.save()
        order.products.set(product_set)
        return order
