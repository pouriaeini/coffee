from ..models import Product
from ..serializers import ProductListSerializer

from coffee.utils.exceptions import OptionException


class ProductServices:
    PRODUCT_OBJ_NONE_VALUE = Product.objects.none()

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_product(pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Product.objects.none()

    @staticmethod
    def get_products(ids: list):
        products = Product.objects.filter(id__in=ids)
        if products.count() != len(ids):
            for p in products:
                if not p.id in ids:
                    raise OptionException
        return products

