"""Test the interaction with the Luftdaten API."""
import httpx
import pytest
from pytest_httpx import HTTPXMock

from luftdaten import Luftdaten

SENSOR_ID = 1

@pytest.mark.asyncio
async def test_timeout(httpx_mock: HTTPXMock):
    """Test if the connection is hitting the timeout."""

    def raise_timeout(request):
        """Set the timeout for the requests."""
        raise httpx.ReadTimeout(
            f"Unable to read within {request.extensions['timeout']}", request=request
        )

    httpx_mock.add_callback(raise_timeout)

    with pytest.raises(httpx.ReadTimeout):
        client = Luftdaten(SENSOR_ID)
        await client.get_data()
