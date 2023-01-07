import json
from abc import ABC


class APIKeyManager(ABC):
    def __init__(self, file_name: str, api_name: str, api_key_name: str = "api_key"):
        self._file_name = file_name
        self._api_name = api_name
        self._api_key_name = api_key_name
        self.api_key = self._get_key(self._api_key_name)

    def _get_key(self, key_name: str) -> str:
        with open(self._file_name) as f:
            data = json.load(f)
            return data[self._api_name][key_name]


class APIWithSecretKeyManager(APIKeyManager):
    def __init__(
        self,
        file_name: str,
        api_name: str,
        api_key_name: str = "api_key",
        secret_key_name: str = "api_secret",
    ):
        super().__init__(file_name, api_name, api_key_name)
        self.secret = self._get_key(secret_key_name)


class DHLKeyManager(APIWithSecretKeyManager):
    def __init__(self):
        super().__init__("where_is_my_parcel/.credentials.json", "dhl")


class MapboxKeyManager(APIKeyManager):
    def __init__(self):
        super().__init__("where_is_my_parcel/.credentials.json", "mapbox")
