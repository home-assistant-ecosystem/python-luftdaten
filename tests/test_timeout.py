"""Test the interaction with the Luftdaten API."""
import httpx
import pytest
from pytest_httpx import HTTPXMock

from luftdaten import Luftdaten
from luftdaten.exceptions import LuftdatenConnectionError

SENSOR_ID = 1

@pytest.mark.asyncio
async def test_connect_timeout(httpx_mock: HTTPXMock):
    """Test if the connection is hitting the timeout during connect."""

    def raise_timeout(request):
        """Set the timeout for the requests."""
        raise httpx.ConnectTimeout(
            f"Unable to connect within {request.extensions['timeout']}", request=request
        )

    httpx_mock.add_callback(raise_timeout)

    with pytest.raises(LuftdatenConnectionError):
        client = Luftdaten(SENSOR_ID)
        await client.get_data()

@pytest.mark.asyncio
async def test_read_timeout(httpx_mock: HTTPXMock):
    """Test if the connection is hitting the timeout during data reading."""

    def raise_timeout(request):
        """Set the timeout for the requests."""
        raise httpx.ReadTimeout(
            f"Unable to read within {request.extensions['timeout']}", request=request
        )

    httpx_mock.add_callback(raise_timeout)

    with pytest.raises(LuftdatenConnectionError):
        client = Luftdaten(SENSOR_ID)
        await client.get_data()
