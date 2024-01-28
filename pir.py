from machine import Pin
import time

pir = Pin(28, Pin.IN)
led = Pin(16, Pin.OUT)

while True:
    state = pir.value()
    print("state:", state)
    if state:
        led.value(1)
    else:
        led.value(0)
        
    time.sleep(1)