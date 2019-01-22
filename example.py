"""Example for getting the data from a station."""
import asyncio

import aiohttp

from luftdaten import Luftdaten

SENSOR_ID = 155


async def main():
    """Sample code to retrieve the data."""
    async with aiohttp.ClientSession() as session:
        data = Luftdaten(SENSOR_ID, loop, session)
        await data.get_data()

        if not await data.validate_sensor():
            print("Station is not available:", data.sensor_id)
            return

        if data.values and data.meta:
            # Print the sensor values
            print("Sensor values:", data.values)

            # Print the coordinates fo the sensor
            print("Location:", data.meta['latitude'], data.meta['longitude'])


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
