"""
Copyright (c) 2017-2018 Fabian Affolter <fabian@affolter-engineering.ch>

Licensed under MIT. All rights reserved.
"""


class LuftdatenError(Exception):
    """General LuftdatenError exception occurred."""

    pass


class LuftdatenConnectionError(LuftdatenError):
    """When a connection error is encountered."""

    pass


class LuftdatenNoDataAvailable(LuftdatenError):
    """When no data is available."""

    pass
