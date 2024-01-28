import time
import network
import machine
import BlynkLib
import math
 
led = machine.Pin(16, machine.Pin.OUT)
pot_pin = machine.ADC(28)
max_val = math.pow(2,16) - 1

ssid = "YOUR_SSID"
password = 'YOUR_PASSWORD'
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

BLYNK_AUTH = 'YOUR_BLYNK_AUTH'
 
# connect the network       
wait = 40
while wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    wait -= 1
    print('waiting for connection...')
    time.sleep(1)
 
# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print(f'connected on {wlan.ifconfig()[0]}')

# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)
 
# Register virtual pin handler
@blynk.on("V1")      #virtual pin V1
def v0_write_handler(value): #read the value
    if int(value[0]) == 1:
        led.value(1)    #turn the led on
    else:
        led.value(0)    #turn the led off

while True:
    pot_val = pot_pin.read_u16() # fetch the digital converted value
    pot_pct = pot_val / max_val  # calculate percentage
    print(str(pot_val) + " -> pct: " + str(pot_pct*100))
    blynk.virtual_write(7, round(pot_pct, 2))
    blynk.run()
    time.sleep(1)