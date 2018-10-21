"""
Copyright (c) 2017-2018 Fabian Affolter <fabian@affolter-engineering.ch>

Licensed under MIT. All rights reserved.
"""
import asyncio

import aiohttp

from luftdaten import Luftdaten


async def main():
    """Sample code to retrieve the data."""
    async with aiohttp.ClientSession() as session:
        data = Luftdaten(155, loop, session)
        await data.get_data()

        if not data.valid_sensor:
            print("Station is not available:", data.sensor_id)
            return

        if data.values and data.meta:
            # Print the sensor values
            print("Sensor values:", data.values)

            # Print the coordinates fo the sensor
            print("Location:", data.meta['latitude'], data.meta['longitude'])


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
