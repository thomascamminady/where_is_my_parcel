from where_is_my_parcel.backend.shipment import DHLShipment


class ExposedDHLShipmentObject:
    def __init__(self, shipment: DHLShipment):
        self._shipment = shipment
        self.id = int(self.get("id"))
        self.service = self.get("service")
        self.origin = self.get("origin")
        self.destination = self.get("destination")
        self.status = self.get("status")
        self.estimatedTimeOfDelivery = self.get("estimatedTimeOfDelivery")
        self.estimatedTimeOfDeliveryRemark = self.get("estimatedTimeOfDeliveryRemark")
        self.details = self.get("details")
        self.events = self._shipment.events

    def to_json(self):
        return {
            "id": self.id,
            "service": self.service,
            "origin": self.origin,
            "destination": self.destination,
            "status": self.status,
            "estimatedTimeOfDelivery": self.estimatedTimeOfDelivery,
            "estimatedTimeOfDeliveryRemark": self.estimatedTimeOfDeliveryRemark,
            "details": self.details,
            "events": [event.to_json() for event in self.events],
        }

    def get(self, key: str) -> str:
        return self._shipment.data[key] if key in self._shipment.data else ""
