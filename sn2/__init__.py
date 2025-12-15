"""Python library for SystemNexa2 device integration."""

from sn2.device import (
    ConnectionStatus,
    Device,
    DeviceInitializationError,
    DeviceUnsupportedError,
    InformationData,
    InformationUpdate,
    OnOffSetting,
    SettingsUpdate,
    StateChange,
)

__version__ = "0.1.2"
__all__ = [
    "ConnectionStatus",
    "Device",
    "DeviceInitializationError",
    "DeviceUnsupportedError",
    "InformationData",
    "InformationUpdate",
    "OnOffSetting",
    "SettingsUpdate",
    "StateChange",
]
