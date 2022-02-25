from django.urls import reverse
from rest_framework.status import HTTP_405_METHOD_NOT_ALLOWED, HTTP_201_CREATED
from rest_framework.test import APITestCase

from cars.models import Car


class RateAcceptanceAPITest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.car = Car(brand="renault", model="lololo")
        cls.car.save()

    def test_rate_list_SHOULD_return_HTTP_405_MEHTOD_NOT_ALLOWED(self):
        url = reverse("rate-list")
        response = self.client.get(path=url)

        self.assertEqual(response.status_code, HTTP_405_METHOD_NOT_ALLOWED)

    def test_rate_create_SHOULD_return_HTTP_405_MEHTOD_NOT_ALLOWED(self):
        url = reverse("rate-list")
        response = self.client.post(
            path=url,
            data={"car": self.car.pk, "rating": 3}
        )

        self.assertEqual(response.status_code, HTTP_201_CREATED)
