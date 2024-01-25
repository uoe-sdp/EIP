import time
from grove.grove_led import GroveLed
from grove.grove_switch import GroveSwitch

# connect to pin 5(slot D5)
PIN   = 5
led = GroveLed(PIN)

# connect to pin 16 (slot D16)
PIN = 16
sw = GroveSwitch(PIN)

while True:
    if sw.state:
        led.on()
    else:
        led.off()
    time.sleep(1)

