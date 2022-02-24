from rest_framework import serializers

from cars.models import Car


class CarSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Car
        fields = ["id", "brand", "model"]
