# python-sn2

Python library for SystemNexa2 device integration.

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
