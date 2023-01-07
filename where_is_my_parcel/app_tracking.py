"""
A flask app that provides the API to the tracking service.
We provide only one route: /track
The route takes a tracking ID and returns the tracking information.
"""
from flask import Flask

from where_is_my_parcel.exposed_shipment_object import ExposedDHLShipmentObject
from where_is_my_parcel.shipment_tracker import DHLShipmentTracker

app = Flask(__name__)


@app.route("/track/<tracking_id>")
def track(tracking_id: str):
    """
    Returns the tracking information for the given tracking ID.
    """
    answer = DHLShipmentTracker().track(tracking_id)
    assert len(answer.shipments) == 1

    shipment = answer.shipments[0]

    return ExposedDHLShipmentObject(shipment).to_json()


if __name__ == "__main__":
    app.run(debug=True)
