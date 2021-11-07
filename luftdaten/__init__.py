"""Wrapper to get the measurings from a Luftdaten station."""
import logging

import httpx

from . import exceptions

_LOGGER = logging.getLogger(__name__)
_RESOURCE = "https://data.sensor.community/airrohr/v1"


class Luftdaten(object):
    """A class for handling the data retrieval."""

    def __init__(self, sensor_id):
        """Initialize the connection."""
        self.sensor_id = sensor_id
        self.data = None
        self.values = {}
        self.meta = {}
        self.url = "{}/{}".format(_RESOURCE, "sensor")

    async def get_data(self):
        """Retrieve the data."""
        url = "{}/{}/".format(self.url, self.sensor_id)

        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(str(url))
        except httpx.ConnectError:
            raise exceptions.LuftdatenConnectionError(f"Connection to {url} failed")

        if response.status_code == httpx.codes.OK:
            try:
                _LOGGER.debug(response.json())
                self.data = response.json()
            except TypeError:
                _LOGGER.error("Can not load data from Luftdaten API")
                raise exceptions.LuftdatenConnectionError(
                    "Unable to get the data from Luftdaten API"
                )

        if not self.data:
            for measurement in self.values.keys():
                self.values[measurement] = None
            return

        try:
            sensor_data = sorted(
                self.data, key=lambda timestamp: timestamp["timestamp"], reverse=True
            )[0]

            for entry in sensor_data["sensordatavalues"]:
                if entry["value_type"] not in self.values.keys():
                    self.values[entry["value_type"]] = None
                for measurement in self.values.keys():
                    if measurement == entry["value_type"]:
                        self.values[measurement] = float(entry["value"])

            self.meta["sensor_id"] = self.sensor_id
            self.meta["longitude"] = float(sensor_data["location"]["longitude"])
            self.meta["latitude"] = float(sensor_data["location"]["latitude"])
            self.meta["altitude"] = float(sensor_data["location"]["altitude"])
        except (TypeError, IndexError):
            raise exceptions.LuftdatenError()

    async def validate_sensor(self):
        """Return True if the sensor ID is valid."""
        return True if self.data else False
