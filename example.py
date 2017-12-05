"""
Copyright (c) 2017 Fabian Affolter <fabian@affolter-engineering.ch>

Licensed under MIT. All rights reserved.
"""
import asyncio
import aiohttp

from luftdaten import Luftdaten


@asyncio.coroutine
def main():
    with aiohttp.ClientSession() as session:
        data = Luftdaten(2154, loop, session)
        yield from data.async_get_data()

        # Print the sensor values
        print("Sensor values:", data.values)

        # Print the coordinates fo the sensor
        print("Location:", data.meta['latitude'], data.meta['longitude'])


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
