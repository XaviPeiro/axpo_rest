from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from cars.models import Car
from cars.services.vpic_client import VPICClient


class CarSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Car
        fields = ["id", "brand", "model"]

    def create(self, validated_data):
        vpi_client = VPICClient()
        brand_and_model_exists = vpi_client.does_brand_and_model_exists(
            brand=validated_data["brand"],
            model=validated_data["model"]
        )

        if brand_and_model_exists is False:
            raise ValidationError("This brand and/or model are not valid")

        result = super(CarSerializer, self).create(validated_data)
        return result