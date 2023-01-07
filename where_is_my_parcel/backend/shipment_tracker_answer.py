from abc import ABC
from typing import Any, Generic
from where_is_my_parcel.backend.shipment import DHLShipment, GenericShipment


class ShipmentTrackerAnswer(ABC, Generic[GenericShipment]):
    def __init__(self) -> None:
        self.shipments: list[GenericShipment] = []


class DHLShipmentTrackerAnswer(ShipmentTrackerAnswer[DHLShipment]):
    def __init__(self, data: dict[str, Any]):
        self.shipments: list[DHLShipment] = [
            DHLShipment(shipment) for shipment in data["shipments"]
        ]
