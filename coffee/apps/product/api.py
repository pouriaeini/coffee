from rest_framework.generics import ListAPIView
from .services.product import ProductServices
from .serializers import ProductListSerializer


class MenuListAPIView(ListAPIView):
    queryset = ProductServices.get_all_products()
    serializer_class = ProductListSerializer

    def get_queryset(self):
        return super(MenuListAPIView, self).get_queryset()
