import http.client
import json
from typing import Any


class HTTPConnector:
    def __init__(
        self,
        connection: str,
        headers: dict[str, str],
        type: str = "GET",
        payload: str = "",
    ):
        self.headers = headers
        self.payload = payload
        self.type = type
        self.connection = connection

    def _request(self, path: str) -> dict[str, Any]:
        conn = http.client.HTTPSConnection(self.connection)
        conn.request(self.type, path, self.payload, self.headers)
        res = conn.getresponse()
        return json.loads(res.read().decode("utf-8"))
