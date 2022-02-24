from django.shortcuts import render
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet


# Create your views here.
from cars.models import Car
from cars.serializers import CarSerializer


class CarViewSet(GenericViewSet, ListModelMixin, CreateModelMixin, DestroyModelMixin, RetrieveModelMixin):
    serializer_class = CarSerializer
    queryset = Car.objects.all()

    def perform_create(self, serializer):
        ...
