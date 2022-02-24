from unittest import TestCase, mock
from unittest.mock import Mock

from rest_framework.status import HTTP_200_OK

from cars.services.vpic_client import VPICClient, NotFoundException


class VPICClientAcceptance(TestCase):

    def test_private_request_method_WITH_existing_brand_SHOULD_return_HTTP_200_OK(self):
        vpi_client = VPICClient()
        response = vpi_client._request(
            method="GET",
            uri="vehicles/GetModelsForMake/VolksWagen?format=json"
        )

        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_private_request_method_WITH_NON_existing_brand_SHOULD_raise_NotFoundException(self):
        vpi_client = VPICClient()
        self.assertRaises(NotFoundException, vpi_client.get_models_for_brand, brand="asdfasdf")


class VPICClientUnitTest(TestCase):

    def test_get_models_for_brand_WITH_existing_brand_SHOULD_return_list_of_models(self):
        vpi_client = VPICClient()
        response = vpi_client.get_models_for_brand(brand="volkswagen")

        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_does_brand_and_model_exists_WITH_NON_existing_SHOULD_return_false(self):
        with mock.patch("cars.services.vpic_client.VPICClient._request") as vpic_request:
            vpic_request.side_effect = Mock(side_effect=NotFoundException)
            vpi_client = VPICClient()
            response = vpi_client.does_brand_and_model_exists(brand="whatever", model="oliwki")

        self.assertFalse(response)

    def test_does_brand_and_model_exists_WITH_existing_SHOULD_return_true(self):
        model = "Routan"
        brand = "VOLKSWAGEN"
        with mock.patch("cars.services.vpic_client.VPICClient._request_json") as vpic_request:
            vpic_request.return_value = {
                "Count": 1,
                "Message": "Response returned successfully",
                "SearchCriteria": "Make:VolksWagen",
                "Results": [{"Make_ID": 482, "Make_Name": "VOLKSWAGEN", "Model_ID": 1951, "Model_Name": "Routan"}]
            }
            vpi_client = VPICClient()
            response = vpi_client.does_brand_and_model_exists(brand=brand, model=model)

        self.assertTrue(response)


