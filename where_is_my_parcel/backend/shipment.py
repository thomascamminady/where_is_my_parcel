from abc import ABC
from typing import Any, TypeVar

from where_is_my_parcel.backend.address_resolver import AddressResolver


class Shipment(ABC):
    pass


class DHLShipment(Shipment):
    class Event:
        def __init__(self, data: dict[str, Any]) -> None:

            try:
                self.timestamp = data["timestamp"]
                self.location = data["location"]["address"]["addressLocality"]
                self.description = data["description"]
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

    def __init__(self, data: dict[str, Any]) -> None:
        self.data = data
        self.events = [DHLShipment.Event(event) for event in self.data["events"]]

    def __str__(self) -> str:
        return "\n".join([str(event) for event in self.events])

    def __repr__(self) -> str:
        return self.__str__()


GenericShipment = TypeVar("GenericShipment", bound=Shipment)
