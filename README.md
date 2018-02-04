# Blinking LED with Micropython :boom: :bulb:

Documenting how I was able to set up and run Micropython on NodeMCU which is a esp8266 board and blink LED.

## Installation

### My setup
* Ubuntu 16.04
* Python 3.6.2

#### Software needed
[esptool](https://github.com/espressif/esptool) - `$ sudo pip install esptool`

[rshell](https://github.com/dhylands/rshell) - `$ sudo pip install rshell`

micropython firmare for esp8266 - [download latest version here](http://micropython.org/download#esp8266) 

main.py in this repo. clone this repo to get it copy the code.

#### How to install

first erase flash using esptool with this command
```bash
esptool.py --port /dev/ttyUSB0 erase_flash
```
deploy the firmware
```bash
esptool.py --port /dev/ttyUSB0 --baud 115200 write_flash --flash_size=detect 0 esp8266-20171101-v1.9.3.bin
```
## Connecting to the board and running code
```bash
rshell -p /dev/ttyUSB0

> cp main.py /pyboard
```
On the nodemcu the onboard LED is on pin 2.

Now restart the board by pressing RST on the board or disconnect usb and reconnect.

LED should be blinking.

Note that ```on``` method of a Pin might turn the LED off and ```off``` might turn it on (or vice versa)

## Credits
[Micropython Documentation on esp8266](http://micropython.org/resources/docs/en/latest/esp8266/index.html)
