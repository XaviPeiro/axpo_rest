from django.urls import reverse
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from rest_framework.test import APITestCase

from cars.models import Car


class CarAcceptanceAPITest(APITestCase):

    def test_car_list(self):
        url = reverse('car-list')
        response = self.client.get(path=url)

        assert response.status_code == HTTP_200_OK

    def test_car_retrieve_WITH_existing_id_SHOULD_return_HTTP_200(self):
        new_car = Car(brand="Renault", model="Something")
        new_car.save()

        url = reverse('car-detail', kwargs={"pk": new_car.pk})
        response = self.client.get(path=url)

        assert response.status_code == HTTP_200_OK

    def test_car_retrieve_WITH_non_existing_id_SHOULD_return_HTTP_404(self):
        url = reverse('car-detail', kwargs={"pk": 1})
        response = self.client.get(path=url)

        assert response.status_code == HTTP_404_NOT_FOUND

    def test_car_insert_WITH_existing_brand_and_model_SHOULD_return_HTTP_201_CREATED(self):
        url = reverse('car-list')
        response = self.client.post(
            path=url,
            format="json",
            data={
                "brand": "Volkswagen",
                "model": "Golf"
            }
        )

        assert response.status_code == HTTP_201_CREATED

    def test_car_delete_WITH_existing_brand_and_model_SHOULD_return_HTTP_201_CREATED(self):
        new_car = Car(brand="Renault", model="Something")
        new_car.save()

        url = reverse('car-detail', kwargs={"pk": new_car.pk})
        response = self.client.delete(path=url)

        assert response.status_code is HTTP_204_NO_CONTENT