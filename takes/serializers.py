from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from takes.models import Product


class ProductSerializer(ModelSerializer):
    # category = CategorySerializer()
    # color = ColorSerializer

    after_sale = serializers.SerializerMethodField()

    def get_after_sale(self, obj):
        price = obj.price
        sale = obj.sale

        if sale is not None and sale > 0:
            after_sale = price - (price * (sale / 100))
        else:
            after_sale = price

        return after_sale

    class Meta:
        model = Product
        fields = '__all__'
