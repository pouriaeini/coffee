from django.test import TestCase

from .order import OrderServices
from ..models import Order


class OrderServiceTestCase(TestCase):
    fixtures = ['product', 'option',]

    def test_new_order(self):
        first_name = "fake first"
        last_name = "fake last"
        email = "fake@fake.com"
        phone_number = "989121231212"
        products = (('pk', 2), )

        result = OrderServices.new_order(first_name, last_name, email, phone_number, products)

        self.assertEqual(result.first_name, first_name)
        self.assertEqual(result.email, email)

        products = result.products.all()
        expected_price = 0
        for p in products:
            expected_price += p.price

        self.assertEqual(expected_price, result.price)
