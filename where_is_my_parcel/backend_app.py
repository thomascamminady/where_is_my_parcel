"""
A flask app that provides the API to the tracking service.
We provide only one route: /track
The route takes a tracking ID and returns the tracking information.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from where_is_my_parcel.backend.exposed_shipment_object import ExposedDHLShipmentObject
from where_is_my_parcel.backend.pretty_json_response import PrettyJSONResponse
from where_is_my_parcel.backend.shipment_tracker import DHLShipmentTracker

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/track/{tracking_id}", response_class=PrettyJSONResponse)
def track(tracking_id: str):
    answer = DHLShipmentTracker().track(tracking_id)
    assert len(answer.shipments) == 1

    shipment = answer.shipments[0]

    return ExposedDHLShipmentObject(shipment)
