from rest_framework import routers

from data_services.views import DataServicesViewSet

router = routers.DefaultRouter()
router.register(prefix=r"data-services/", viewset=DataServicesViewSet)
