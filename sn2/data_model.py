"""Data models for device information and settings."""

from dataclasses import dataclass
from typing import Any

from .constants import LIGHT_MODELS


@dataclass(frozen=True, slots=True)
class InformationData:
    """Device information data container."""

    dimmable: bool
    hw_version: str | None
    model: str
    name: str
    sw_version: str | None
    unique_id: str
    uptime_seconds: int | None
    wifi_dbm: int | None
    wifi_ssid: str | None

    @staticmethod
    def from_device_dict(
        info: dict[str, Any],
    ) -> "InformationData":
        """Create InformationData from a dict object."""
        uniq_id = info.get("lcu")
        if uniq_id is None:
            msg = "lcu (unique id) cannot be None, broken/corrupt device?"
            raise ValueError(msg)
        hwm = info.get("hwm")
        if hwm is None:
            msg = "hwm (model) cannot be None, broken/corrupt device?"
            raise ValueError(msg)
        name = info.get("n")
        if name is None:
            msg = "n (name) cannot be None, broken/corrupt device?"
            raise ValueError(msg)
        hw_version = info.get("nhwv")
        uptime_seconds = info.get("u")
        return InformationData(
            model=hwm,
            sw_version=info.get("nswv"),
            hw_version=str(hw_version) if hw_version is not None else None,
            name=name,
            wifi_dbm=info.get("wr"),
            wifi_ssid=info.get("ws"),
            unique_id=uniq_id,
            dimmable=hwm in LIGHT_MODELS,
            uptime_seconds=uptime_seconds,
        )

@dataclass(frozen=True, slots=True)
class Settings433Mhz:
    """Represents 433 MHz settings for the device."""
    disable_433: int | None = None
    transmitter_send_off_dim_level: float | None = None
        
@dataclass(frozen=True, slots=True)
class Settings:
    """Represents device settings with various configuration attributes."""

    name: str | None = None
    disable_physical_button: int | None = None
    disable_led: int | None = None
    diy_mode: int | None = None
    dimmer_minimum_level: float | None = None
    settings_433_mhz: Settings433Mhz | None = None

    

    @staticmethod
    def from_device_dict(data: dict) -> "Settings":
        """Create a Settings instance from a device dictionary."""
        return Settings(
            name=data.get("name"),
            disable_physical_button=data.get("disable_physical_button"),
            disable_led=data.get("disable_led"),
            diy_mode=data.get("diy_mode"),
            dimmer_minimum_level=data.get("dimmer_min_dim"),
            settings_433_mhz=Settings433Mhz(
                disable_433=data.get("disable_433"),
                transmitter_send_off_dim_level=data.get("dimmer_off_level"),
            )
        )
