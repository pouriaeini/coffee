from rest_framework import serializers

from coffee.apps.product.serializers import ProductSerializer

from .services.order import OrderServices
from .models import Order


class OrderViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class NewOrderSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=32)
    last_name = serializers.CharField(max_length=32)
    phone_number = serializers.CharField(max_length=32, required=False)
    email = serializers.EmailField()
    status = serializers.BooleanField(required=False, read_only=True)
    products = serializers.ListSerializer(child=ProductSerializer())

    def update(self, instance, validated_data):
        raise NotImplementedError

    def create(self, validated_data):
        instance = OrderServices.new_order(**self.validated_data)
        return instance
