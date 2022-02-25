# Create your views here.
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import GenericViewSet

from data_services.models import RatedTimesCar
from data_services.serializers import RateSerializer
from data_services.services.metrics import Metrics


class DataServicesViewSet(GenericViewSet):
    queryset = RatedTimesCar.objects

    @action(detail=False, methods=["GET"])
    def popular(self, request: Request, *args, **kwargs):
        m = Metrics()
        populars = m.get_most_frequently_voted(q=3)
        res = RateSerializer(populars, many=True).data
        return Response(status=HTTP_200_OK, data=res)


