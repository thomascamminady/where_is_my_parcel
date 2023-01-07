import http.client
import json
from abc import ABC, abstractmethod
from typing import Generic

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


class DHLShipmentTracker(ShipmentTracker[DHLShipment]):
    def __init__(self):
        self._key_manager = DHLKeyManager()
        self._headers = {
            "DHL-API-Key": self._key_manager.api_key,
            "DHL-API-Secret": self._key_manager.secret,
            "Content-Type": "application/json",
        }
        self._payload = ""

    def _track(self, tracking_number: str) -> DHLShipmentTrackerAnswer:
        conn = http.client.HTTPSConnection("api-eu.dhl.com")

        conn.request(
            "GET",
            f"/track/shipments?trackingNumber={tracking_number}",
            self._payload,
            self._headers,
        )
        res = conn.getresponse()
        data = json.loads(res.read().decode("utf-8"))
        return DHLShipmentTrackerAnswer(data)
