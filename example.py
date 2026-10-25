"""Example for getting the data from a station."""
import asyncio

import httpx

from luftdaten import Luftdaten

SENSOR_ID = 152
SENSOR_IDS = (152, 153)


async def main():
    """Sample code to retrieve the data."""
    data = Luftdaten(SENSOR_ID)
    await data.get_data()

    if not await data.validate_sensor():
        print("Station is not available:", data.sensor_id)
        return

    if data.values and data.meta:
        # Print the sensor values
        print("Sensor values:", data.values)

        # Print the coordinates fo the sensor
        print(
            "Location:",
            data.meta["latitude"],
            data.meta["longitude"],
            data.meta["altitude"],
        )


async def main_with_httpx_client():
    """Sample code using an existing HTTPX client for multiple sensors."""
    async with httpx.AsyncClient() as httpx_client:
        # Reuse the same HTTPX session for all sensors.
        for sensor_id in SENSOR_IDS:
            data = Luftdaten(sensor_id, httpx_client=httpx_client)
            await data.get_data()

            if not await data.validate_sensor():
                print("Station is not available:", data.sensor_id)
                continue

            if data.values and data.meta:
                print("Sensor values:", data.values)
                print(
                    "Location:",
                    data.meta["latitude"],
                    data.meta["longitude"],
                    data.meta["altitude"],
                )


if __name__ == "__main__":
    asyncio.run(main())
