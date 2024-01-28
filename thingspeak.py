import machine
import urequests
import network, time
import math
 
pot_pin = machine.ADC(28)
max_val = math.pow(2,16) - 1

HTTP_HEADERS = {'Content-Type': 'application/json'} 
THINGSPEAK_WRITE_API_KEY = 'YOUR_THINGSPEAK_WRITE_API_KEY'
 
ssid = 'YOUR_SSID'
password = 'YOUR_PASSWORD'
wlan=network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)
while not wlan.isconnected():
    print('waiting for connection...')
print(f'connected on {wlan.ifconfig()[0]}')

while True:
    time.sleep(5) 
    pot_val = pot_pin.read_u16()
    pot_pct = round(pot_val / max_val, 2)
    data = {'field1': pot_pct} 
    request = urequests.post('http://api.thingspeak.com/update?api_key='+THINGSPEAK_WRITE_API_KEY, json=data, headers=HTTP_HEADERS)  
    request.close() 
    print(data)