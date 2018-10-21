"""
Copyright (c) 2017-2018 Fabian Affolter <fabian@affolter-engineering.ch>

Licensed under MIT. All rights reserved.
"""
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
        self.values = {
                'humidity': None,
                'P1': None,
                'P2': None,
                'pressure': None,
                'temperature': None,
            }
        self.meta = {}

    async def get_data(self):
        """Retrieve the data."""
        url = '{}/{}/{}/'.format(_RESOURCE, 'sensor', self.sensor_id)

        try:
            with async_timeout.timeout(5, loop=self._loop):
                response = await self._session.get(url)

            _LOGGER.debug(
                "Response from luftdaten.info: %s", response.status)
            data = await response.json()
            _LOGGER.debug(data)
        except (asyncio.TimeoutError, aiohttp.ClientError):
            _LOGGER.error("Can not load data from luftdaten.info")
            raise exceptions.LuftdatenConnectionError()

        if not data:
            self.values = self.meta = None
            return

        try:
            sensor_data = sorted(
                data, key=lambda timestamp: timestamp['timestamp'],
                reverse=True)[0]

            for entry in sensor_data['sensordatavalues']:
                for measurement in self.values.keys():
                    if measurement == entry['value_type']:
                        self.values[measurement] = float(entry['value'])

            self.meta['sensor_id'] = self.sensor_id
            self.meta['longitude'] = float(
                sensor_data['location']['longitude'])
            self.meta['latitude'] = float(sensor_data['location']['latitude'])
        except (TypeError, IndexError):
            raise exceptions.LuftdatenError()

    @property
    def valid_sensor(self):
        """Return True if the sensor ID is valid."""
        return True if self.values else False
