"""Wrapper to get the measurings from a Luftdaten station."""
import asyncio
import logging

import aiohttp
import async_timeout

from . import exceptions

_LOGGER = logging.getLogger(__name__)
_RESOURCE = 'https://api.luftdaten.info/v1'


class Luftdaten(object):
    """A class for handling the data retrieval."""

    def __init__(self, sensor_id, loop, session):
        """Initialize the connection."""
        self._loop = loop
        self._session = session
        self.sensor_id = sensor_id
        self.data = None
        self.values = {}
        self.meta = {}
        self.url = '{}/{}'.format(_RESOURCE, 'sensor')

    async def get_data(self):
        """Retrieve the data."""
        try:
            url = '{}/{}/'.format(self.url, self.sensor_id)
            _LOGGER.debug(
                "Requesting luftdaten.info: %s", url)
            with async_timeout.timeout(60, loop=self._loop):
                response = await self._session.get(url)

            _LOGGER.debug(
                "Response from luftdaten.info: %s", response.status)
            self.data = await response.json()
            _LOGGER.debug(self.data)
        except (asyncio.TimeoutError, aiohttp.ClientError):
            _LOGGER.error("Can not load data from luftdaten.info")
            raise exceptions.LuftdatenConnectionError()

        if not self.data:
            for measurement in self.values.keys():
                self.values[measurement] = None
            return

        try:
            sensor_data = sorted(
                self.data, key=lambda timestamp: timestamp['timestamp'],
                reverse=True)[0]

            for entry in sensor_data['sensordatavalues']:
                if entry['value_type'] not in self.values.keys():
                    self.values[entry['value_type']] = None
                for measurement in self.values.keys():
                    if measurement == entry['value_type']:
                        self.values[measurement] = float(entry['value'])

            self.meta['sensor_id'] = self.sensor_id
            self.meta['longitude'] = float(
                sensor_data['location']['longitude'])
            self.meta['latitude'] = float(sensor_data['location']['latitude'])
        except (TypeError, IndexError):
            raise exceptions.LuftdatenError()

    async def validate_sensor(self):
        """Return True if the sensor ID is valid."""
        return True if self.data else False
