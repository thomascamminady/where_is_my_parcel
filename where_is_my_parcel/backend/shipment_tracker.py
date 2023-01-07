from abc import ABC, abstractmethod
from typing import Generic

from where_is_my_parcel.backend.http_connector import HTTPConnector
from where_is_my_parcel.backend.keymanager import DHLKeyManager
from where_is_my_parcel.backend.shipment import DHLShipment, GenericShipment
from where_is_my_parcel.backend.shipment_tracker_answer import (
    DHLShipmentTrackerAnswer,
    ShipmentTrackerAnswer,
)


class ShipmentTracker(ABC, Generic[GenericShipment]):
    def track(
        self, tracking_number: str | int
    ) -> ShipmentTrackerAnswer[GenericShipment]:
        if isinstance(tracking_number, int):
            tracking_number = str(tracking_number)

        return self._track(tracking_number)

    @abstractmethod
    def _track(self, tracking_number: str) -> ShipmentTrackerAnswer[GenericShipment]:
        pass


class DHLShipmentTracker(ShipmentTracker[DHLShipment], HTTPConnector):
    def __init__(self):
        self._key_manager = DHLKeyManager()
        super().__init__(
            "api-eu.dhl.com",
            {
                "DHL-API-Key": self._key_manager.api_key,
                "DHL-API-Secret": self._key_manager.secret,
                "Content-Type": "application/json",
            },
            "GET",
            "",
        )

    def _track(self, tracking_number: str) -> DHLShipmentTrackerAnswer:
        path = f"/track/shipments?trackingNumber={tracking_number}"
        data = self._request(path)
        return DHLShipmentTrackerAnswer(data)
