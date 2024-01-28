from machine import Pin
from utime import sleep

led = Pin("LED", Pin.OUT)

print("LED starts flashing...")
while True:
    try:
        led.value(True)
        sleep(1)
        led.value(False)
        sleep(1)
    except KeyboardInterrupt:
        break
led.off()
print("Finished.")
