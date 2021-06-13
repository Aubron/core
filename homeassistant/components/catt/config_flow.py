"""Config flow for Cast All The Things."""
import logging

from catt import discovery as cattDiscovery

from homeassistant.core import HomeAssistant
from homeassistant.helpers import config_entry_flow

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)


async def _async_has_devices(hass: HomeAssistant) -> bool:
    """Return if there are devices that can be discovered."""
    # TODO Check if there are any devices that can be discovered in the network.
    devices = await hass.async_add_executor_job(cattDiscovery.get_cast_devices_info)
    _LOGGER.debug("media scan", devices)
    return len(devices) > 0


config_entry_flow.register_discovery_flow(
    DOMAIN, "Cast All The Things", _async_has_devices
)
