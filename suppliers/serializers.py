from rest_framework import serializers

from suppliers.models import Suppliers


class SuppliersSerializers(serializers.ModelSerializer):

    class Meta:
        model = Suppliers
        fields = "__all__"
