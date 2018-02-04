import machine
import time

pin = machine.Pin(2, machine.Pin.OUT)

def blink():
    while True:
        time.sleep(1)
        pin.on()
        time.sleep(1)
        pin.off()

blink()