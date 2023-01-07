from where_is_my_parcel.backend.address_resolver_answer import AddressResolverAnswer
from where_is_my_parcel.backend.http_connector import HTTPConnector
from where_is_my_parcel.backend.keymanager import MapboxKeyManager


class AddressResolver(HTTPConnector):
    def __init__(self):
        self._key_manager = MapboxKeyManager()
        super().__init__(
            "api.mapbox.com",
            {"Content-Type": "application/json"},
            "GET",
            "",
        )

    def resolve(self, address: str) -> AddressResolverAnswer:
        address = address.replace(" ", "%20")
        path = f"/geocoding/v5/mapbox.places/{address}.json?limit=1&types=place&access_token={self._key_manager.api_key}"
        data = self._request(path)
        return AddressResolverAnswer(data)
