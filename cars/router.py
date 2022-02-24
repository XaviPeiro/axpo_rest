from rest_framework import routers

from cars.views import CarViewSet

router = routers.DefaultRouter()
router.register(prefix=r"cars", viewset=CarViewSet)