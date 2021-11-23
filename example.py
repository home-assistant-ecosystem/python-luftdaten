"""Example for getting the data from a station."""
import asyncio

from luftdaten import Luftdaten

SENSOR_ID = 152


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

        
if __name__ == "__main__":
    asyncio.run(main())
