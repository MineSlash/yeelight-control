# Yeelight Control
You can easily control your Yeelight Smart lamp at home with this Python code.
## Installation
* Download smarthome.py from https://github.com/MineSlash/yeelight-control/.
## Usage
To use the script, you must first obtain the token of your Yeelight lamp from the Xiaomi website, as well as its local IP address.

The simplest way to acquire the tokens is by using the miiocli cloud command, which fetches them for you from your cloud account using [micloud](https://github.com/Squachen/micloud/):
```
miiocli cloud
Username: example@example.com
Password:

== name of the device (Device offline ) ==
    Model: example.device.v1
    Token: b1946ac92492d2347c6235b4d2611184
    IP: 192.168.8.150 (mac: ab:cd:ef:12:34:56)
    DID: 123456789
    Locale: cn
```
To import, use this:
```
>>> from smarthome import Lamp
```
After that, you need to initialize your Lamp:
```
>>> ip = "192.168.8.150"
>>> token = "b1946ac92492d2347c6235b4d2611184"
>>> device = Lamp(ip, token)
```
### Device status
Get status
```
>>> device.status
>>> device.ambient.status
>>> device.light.status
```
Set status
```
>>> device.status = (True|False|1|0)
>>> device.ambient.status = (True|False|1|0)
>>> device.light.status = (True|False|1|0)
```
### Ambient-light/Lamp color
Get color
```
>>> device.ambient.color
>>> device.light.color
```
Set color
```
>>> device.ambient.color = (1 - 16777215 | Hex color code)
>>> device.light.color = (2700 - 6500)
```
### Ambient-light/Lamp brightness
Get brightness
```
>>> device.ambient.brightness
>>> device.light.brightness
```
Set brightness
```
>>> device.ambient.brightness = (1 - 100)
>>> device.light.brightness = (1 - 100)
```
### Ambient-light saturiation
Get saturation
```
>>> device.ambient.saturability
```
Set saturation
```
>>> device.ambient.saturability = (1 - 100)
```
Tested on Yeelight Arwen Ceiling Light 550C.
