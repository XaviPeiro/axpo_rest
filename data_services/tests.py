from django.test import TestCase
from django.urls import reverse
from rest_framework.status import HTTP_200_OK
from rest_framework.test import APITestCase

# Create your tests here.
from cars.models import Car
from data_services.services.metrics import Metrics
from rate.models import Rate


class DataServicesAcceptanceAPITest(APITestCase):

    def test_popular_endpoint_WITH_get_SOULD_return_HTTP_200_OK(self):
        url = reverse("ratedtimescar-popular")
        response = self.client.get(path=url)

        self.assertEqual(response.status_code, HTTP_200_OK)


class PopularUnitTestAPITest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.most_voted_1 = Car(brand="X", model="jojojojo")
        cls.most_voted_2 = Car(brand="A", model="A")
        cls.most_voted_3 = Car(brand="A", model="B")
        cls.most_voted_4 = Car(brand="Z", model="1")
        cls.most_voted_5 = Car(brand="Z", model="2")
        cls.most_voted_1.save()
        cls.most_voted_2.save()
        cls.most_voted_3.save()
        cls.most_voted_4.save()
        cls.most_voted_5.save()

        for i in range(7):
            Rate(car=cls.most_voted_1, rating=5).save()

        for i in range(5):
            Rate(car=cls.most_voted_2, rating=4).save()

        for i in range(3):
            Rate(car=cls.most_voted_3, rating=3).save()

    def test_popular_method_SOULD_most_voted_cars(self):
        m = Metrics()
        populars = m.get_most_frequently_voted(q=3)
        cars_id = list(map(lambda x: x.car_id, list(populars)))

        self.assertIn(self.most_voted_1.id, cars_id)
        self.assertIn(self.most_voted_2.id, cars_id)
        self.assertIn(self.most_voted_3.id, cars_id)
        self.assertNotIn(self.most_voted_4.id, cars_id)
        self.assertNotIn(self.most_voted_5.id, cars_id)
