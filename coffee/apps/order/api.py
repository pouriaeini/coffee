from rest_framework import views
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import NewOrderSerializer, OrderViewSerializer
from .services.order import OrderServices


class NewOrderCreateAPIView(views.APIView):

    def post(self, request, *args, **kwargs):
        serializer = NewOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_order_obj = serializer.create(serializer.validated_data)
        serializer = OrderViewSerializer(new_order_obj)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class OrderViewAPIView(RetrieveAPIView):
    queryset = OrderServices.get_all_active_orders()
    serializer_class = OrderViewSerializer
    lookup_url_kwarg = 'pk'


class CancelOrderAPIView(views.APIView):
    def get(self, request, pk, *args, **kwargs):
        OrderServices.cancel_order(pk)
        return Response(status=status.HTTP_200_OK, )


class UpdateOrderAPIView(views.APIView):
    def post(self, request, pk, *args, **kwargs):
        serializer = NewOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = OrderServices.update_order(pk, **serializer.validated_data)
        serializer = OrderViewSerializer(order)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
