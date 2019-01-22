"""Exceptions for the Luftdaten Wrapper."""


class LuftdatenError(Exception):
    """General LuftdatenError exception occurred."""

    pass


class LuftdatenConnectionError(LuftdatenError):
    """When a connection error is encountered."""

    pass


class LuftdatenNoDataAvailable(LuftdatenError):
    """When no data is available."""

    pass
