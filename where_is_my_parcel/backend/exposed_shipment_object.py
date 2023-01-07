from where_is_my_parcel.backend.shipment import DHLShipment


class ExposedDHLShipmentObject:
    def __init__(self, shipment: DHLShipment):
        self.id = int(self.get(shipment, "id"))
        self.service = self.get(shipment, "service")
        self.origin = self.get(shipment, "origin")
        self.destination = self.get(shipment, "destination")
        self.status = self.get(shipment, "status")
        self.estimatedTimeOfDelivery = self.get(shipment, "estimatedTimeOfDelivery")
        self.estimatedTimeOfDeliveryRemark = self.get(
            shipment, "estimatedTimeOfDeliveryRemark"
        )
        self.details = self.get(shipment, "details")
        self.events = shipment.events

    def get(self, shipment: DHLShipment, key: str) -> str:
        return shipment.data[key] if key in shipment.data else ""
