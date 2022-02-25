from django.shortcuts import render

# Create your views here.
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from rate.models import Rate
from rate.serializers import RateSerializer


class RateViewSet(GenericViewSet, CreateModelMixin):
    serializer_class = RateSerializer
    queryset = Rate.objects

