from abc import ABC
from typing import Any, TypeVar

import pandas as pd

from where_is_my_parcel.backend.address_resolver import AddressResolver


class Shipment(ABC):
    pass


class DHLShipment(Shipment):
    class Event:
        def __init__(self, data: dict[str, Any]) -> None:
            self._data = data
            try:
                self.timestamp = pd.to_datetime(self._data["timestamp"])  # type: ignore
                self.location = self._data["location"]["address"]["addressLocality"]
                self.description = self._data["description"]
                address = AddressResolver().resolve(self.location)
                self.resolved_location = address.name
                self.latitude = address.latitude
                self.longitude = address.longitude
                self.successfully_resolved = address.successfully_resolved
            except IndexError:
                self.timestamp = ""
                self.location = ""
                self.description = ""
                self.resolved_location = ""
                self.latitude = ""
                self.longitude = ""
                self.successfully_resolved = False

        def __str__(self) -> str:
            return f"{self.timestamp}, {self.resolved_location}: {self.description}"

        def to_json(self) -> dict[str, Any]:
            return {
                "timestamp": self.timestamp,
                "location": self.location,
                "description": self.description,
                "resolved_location": self.resolved_location,
                "latitude": self.latitude,
                "longitude": self.longitude,
                "successfully_resolved": self.successfully_resolved,
            }

    def __init__(self, data: dict[str, Any]) -> None:
        self.data = data
        self.events = [DHLShipment.Event(event) for event in self.data["events"]]

    def __str__(self) -> str:
        return "\n".join([str(event) for event in self.events])

    def __repr__(self) -> str:
        return self.__str__()


GenericShipment = TypeVar("GenericShipment", bound=Shipment)
