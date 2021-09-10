from ..models import Product


class ProductServices:
    @staticmethod
    def get_all_products():
        return Product.objects.all()
