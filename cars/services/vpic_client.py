import requests
from urllib import parse


class NotFoundException(Exception):
    ...

# Serializer for the response wether data would be used
# Move this to an independent service if it is used for other components
class VPICClient:
    url: str = "https://vpic.nhtsa.dot.gov/api/"

    def _request(self, method: str, uri: str) -> dict:
        response = requests.request(
            method=method,
            url=f"{self.url}{uri}"
        )
        return response

    def _request_json(self, method: str, uri: str) -> dict:
        uri += f"?{parse.urlencode({'format': 'json'})}"

        response = self._request(
            method=method,
            uri=uri
        )

        if response.json()["Count"] == 0:
            raise NotFoundException

        return response

    def get_models_for_brand(self, brand: str):
        endpoint = "vehicles/GetModelsForMake/"
        uri = f"{endpoint}/{brand}"

        response = self._request_json(method="GET", uri=uri)
        return response

    def does_brand_and_model_exists(self, brand: str, model: str) -> bool:
        try:
            response = self.get_models_for_brand(brand=brand)
        except NotFoundException:
            return False

        return len(list(filter(lambda x: x["Model_Name"].casefold() == model.casefold(), response["Results"]))) > 0




