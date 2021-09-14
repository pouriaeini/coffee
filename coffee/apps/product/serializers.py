from rest_framework import serializers
from .models import Product, Option


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = "__all__"


class ProductListSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'options']


class ProductSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    option = serializers.CharField()
    # TODO check option is valid for id

    def update(self, instance, validated_data):
        raise NotImplementedError

    def create(self, validated_data):
        raise NotImplementedError
