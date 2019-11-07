from typing import List
import pyppeteer.connection
from pyppeteer.page import Page
from pyppeteer.browser import BrowserContext


def disable_timeout():
    """prevents pyppeteer from killing the connection"""
    original_method = pyppeteer.connection.websockets.client.connect

    def _new_method(*args, **kwargs):
        kwargs['ping_interval'] = None
        kwargs['ping_timeout'] = None
        return original_method(*args, **kwargs)
    pyppeteer.connection.websockets.client.connect = _new_method


def add_geolocation():
    """adds gps geolocation spoofing functionality"""

    async def _set_geolocation(self: Page, longitude: float, latitude: float, accuracy: float):
        if longitude < -180 or longitude > 180:
            raise ValueError(f"Invalid longitude {longitude}: must be in [-180, 180].")
        if latitude < -90 or latitude > 90:
            raise ValueError(f"Invalid latitude {latitude}: must be in [-90, 90].")
        if accuracy < 0:
            raise ValueError(f"Invalid accuracy {longitude}: must be in [0, Inf].")
        await self._client.send('Emulation.setGeolocationOverride',
                                {"longitude": longitude,
                                 "latitude": latitude,
                                 "accuracy": accuracy})
    Page.setGeolocation = _set_geolocation


def add_permissions():
    """adds permission functionality"""

    async def _clear_permission_overrides(self: BrowserContext):
        await self._browser._connection.send(
            'Browser.resetPermissions',
            {'browserContextId': self._id})

    async def _override_permissions(self: BrowserContext, origin: str, permissions: List[str]):
        await self._browser._connection.send('Browser.grantPermissions',
                                             {'browserContextId': self._id,
                                              'origin': origin,
                                              'permissions': permissions})
    BrowserContext.clearPermissionOverrides = _clear_permission_overrides
    BrowserContext.overridePermissions = _override_permissions
