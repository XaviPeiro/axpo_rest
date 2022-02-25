from rest_framework import routers

from rate.views import RateViewSet

router = routers.DefaultRouter()
router.register(prefix=r"rate", viewset=RateViewSet)
