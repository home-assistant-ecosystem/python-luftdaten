"""Test the interaction with the Luftdaten API."""
import pytest
from pytest_httpx import HTTPXMock

from luftdaten import Luftdaten

import httpx

SENSOR_ID = 1

RESPONSE_VALID = [
    {
        "sensor": {
            "sensor_type": {"manufacturer": "various", "name": "DHT22", "id": 9},
            "pin": "7",
            "id": 152,
        },
        "timestamp": "2021-11-07 11:16:45",
        "sampling_rate": None,
        "sensordatavalues": [
            {"value": "10.50", "id": 16932663249, "value_type": "temperature"},
            {"value": "79.30", "id": 16932663267, "value_type": "humidity"},
        ],
        "id": 7706863277,
        "location": {
            "country": "DE",
            "latitude": "48.792",
            "exact_location": 0,
            "altitude": "326.9",
            "longitude": "9.164",
            "indoor": 0,
            "id": 68,
        },
    },
    {
        "sensor": {
            "sensor_type": {"manufacturer": "various", "name": "DHT22", "id": 9},
            "pin": "7",
            "id": 152,
        },
        "timestamp": "2021-11-07 11:14:13",
        "sampling_rate": None,
        "sensordatavalues": [
            {"value": "10.50", "id": 16932614294, "value_type": "temperature"},
            {"value": "80.60", "id": 16932614337, "value_type": "humidity"},
        ],
        "id": 7706841422,
        "location": {
            "country": "DE",
            "latitude": "48.792",
            "exact_location": 0,
            "altitude": "326.9",
            "longitude": "9.164",
            "indoor": 0,
            "id": 68,
        },
    },
]


@pytest.mark.asyncio
async def test_sensor_values(httpx_mock: HTTPXMock):
    """Test the sensor values."""
    httpx_mock.add_response(json=RESPONSE_VALID)

    client = Luftdaten(SENSOR_ID)
    await client.get_data()

    assert client.values == {"temperature": 10.5, "humidity": 79.3}


@pytest.mark.asyncio
async def test_meta(httpx_mock: HTTPXMock):
    """Test the meta information."""
    httpx_mock.add_response(json=RESPONSE_VALID)

    client = Luftdaten(SENSOR_ID)
    await client.get_data()

    assert client.meta["sensor_id"] == 1
    assert client.meta["latitude"] == 48.792
    assert client.meta["longitude"] == 9.164
    assert client.meta["altitude"] == 326.9
