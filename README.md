# python-sn2

Python library for SystemNexa2 device integration.

This package provides a client library for communicating with SystemNexa2 smart home
devices over WebSocket and REST APIs. It supports device discovery, real-time state
updates, brightness control, and configuration management.

Supported Devices
-----------------
- Switches: WBR-01
- Plugs: WPR-01, WPO-01
- Lights: WBD-01, WPD-01

Key Features
------------
- Asynchronous communication via WebSocket and REST
- Real-time device state updates
- Brightness control for dimmable devices
- Device settings management (433MHz, LED, DIY mode, etc.)
- Automatic reconnection handling
- Error handling and logging

## Installation

```bash
pip install python-sn2
```

## Usage

```python
from sn2.device import Device

# Create a device instance
device = Device(ip="192.168.1.100")

# Initialize the device
await device.initialize()

# Connect to the device
await device.connect()

# Set brightness
await device.set_brightness(0.75)

# Get device information
info = await device.get_info()
print(f"Device: {info.information.name}")

# Disconnect
await device.disconnect()
```

## Development

Install development dependencies:

```bash
pip install -e ".[dev]"
```

Run tests:

```bash
pytest
```

## License

MIT License
