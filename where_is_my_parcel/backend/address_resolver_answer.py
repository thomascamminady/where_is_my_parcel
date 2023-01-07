from typing import Any


class AddressResolverAnswer:
    def __init__(self, data: dict[str, Any]):
        self._data = data
        try:
            self.name = self._data["features"][0]["place_name"]
            self.longitude = float(self._data["features"][0]["center"][0])
            self.latitude = float(self._data["features"][0]["center"][1])
            self.successfully_resolved = True
        except IndexError:
            self.name = ""
            self.longitude = 0.0
            self.latitude = 0.0
            self.successfully_resolved = False

    def __str__(self):
        return f"{self.name} (lon={self.longitude}, lat={self.latitude})"

    def __repr__(self):
        return self.__str__()
