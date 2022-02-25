from rest_framework import serializers

from cars.models import Car


class CarRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ("id", "brand", "model")


class RateSerializer(serializers.ModelSerializer):
    car = CarRateSerializer(many=False)
    rates_number = serializers.IntegerField(source="times_voted")

    class Meta:
        fields = ("car", "rates_number")