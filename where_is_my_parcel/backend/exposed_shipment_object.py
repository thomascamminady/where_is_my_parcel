from where_is_my_parcel.backend.shipment import DHLShipment


class ExposedDHLShipmentObject:
    def __init__(self, shipment: DHLShipment):
        self.id = int(self.get(shipment, "id"))
        self.estimatedTimeOfDelivery = self.get(shipment, "estimatedTimeOfDelivery")
        self.estimatedTimeOfDeliveryRemark = self.get(
            shipment, "estimatedTimeOfDeliveryRemark"
        )
        self.events = shipment.events
        self.status = self.get(shipment, "status")
        self.origin = self.get(shipment, "origin")
        self.destination = self.get(shipment, "destination")
        self.details = self.get(shipment, "details")
        self.service = self.get(shipment, "service")

    def get(self, shipment: DHLShipment, key: str) -> str:
        return shipment.data[key] if key in shipment.data else ""
