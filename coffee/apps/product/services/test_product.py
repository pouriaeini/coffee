from django.test import TestCase

from coffee.utils.exceptions import OptionException
from .product import ProductServices
from ..models import Product


class ProductServiceTestCase(TestCase):
    fixtures = ['product', 'option']

    def test_get_all_products(self):
        result = ProductServices.get_all_products()

        expect = Product.objects.all()
        self.assertListEqual(list(result), list(expect))

    def test_get_product_without_non_value(self):
        result = ProductServices.get_product(2)

        expect = Product.objects.first()

        self.assertEqual(result.id, expect.id)

    def test_get_product_with_non_value(self):
        result = ProductServices.get_product(100)

        self.assertFalse(result.exists())

    def test_get_products_without_exceptions(self):
        expect = Product.objects.all()
        ids = [p.id for p in expect]
        result = ProductServices.get_products(ids)

        self.assertListEqual(list(result), list(expect))

    # def test_get_products_with_exceptions(self):
    #     self.assertRaises(OptionException, ProductServices.get_products, ids=[1,100])
