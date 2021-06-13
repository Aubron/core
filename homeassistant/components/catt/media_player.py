"""Provide functionality to interact with Cast devices on the network."""
from homeassistant.components.media_player import SUPPORT_TURN_ON, MediaPlayerEntity


class CattPlayer(MediaPlayerEntity):
    """Representation of a Cast device on the network."""

    def __init__(self) -> None:
        """Initialize object."""
        super().__init__()

    @property
    def supported_features(self):
        """Flag supported media features."""
        return [SUPPORT_TURN_ON]

    @property
    def device_class(self):
        """Describe device class."""
        return "tv"
