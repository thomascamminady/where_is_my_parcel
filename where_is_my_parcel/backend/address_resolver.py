from where_is_my_parcel.backend.address_resolver_answer import AddressResolverAnswer
from where_is_my_parcel.backend.keymanager import MapboxKeyManager
import http.client
import json


class AddressResolver(object):
    def __init__(self):
        self._key_manager = MapboxKeyManager()

    def resolve(self, address: str) -> AddressResolverAnswer:

        conn = http.client.HTTPSConnection("api.mapbox.com")

        address = address.replace(" ", "%20")

        conn.request(
            "GET",
            f"/geocoding/v5/mapbox.places/{address}.json?limit=1&types=place&access_token={self._key_manager.api_key}",
        )
        res = conn.getresponse()
        data = json.loads(res.read().decode("utf-8"))
        return AddressResolverAnswer(data)
