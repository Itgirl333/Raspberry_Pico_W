import machine
import network
import urequests
import time
import math

ssid = "YOUR_SSID"
password = 'YOUR_PASSWORD'

pot_pin = machine.ADC(28)
max_val = math.pow(2,16) - 1

def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        print('Waiting for connection...')
        time.sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    
connect()

firebase_url = "YOUR_FIREBASE_URL"
auth_data = {
    "email": "YOUR_EMAIL",
    "password": "YOUR_PASSWORD",
    "returnSecureToken": True
    }

auth_response = urequests.post("https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=YOUR_KEY", json=auth_data)
auth_response_data = auth_response.json()
#print(auth_response_data)
auth_response.close()
local_id = auth_response_data.get('localId')
#print(local_id)

response = urequests.get(firebase_url)
data_from_db = response.json()
response.close()
print(f"Get data from firebase: {data_from_db}")

while True:
    pot_val = pot_pin.read_u16()
    pot_pct = round(pot_val / max_val, 2)
    data_to_db = {'sensor': pot_pct}
    print(f"Send data to firebase: {data_to_db}")
    response = urequests.post(firebase_url, json=data_to_db)
    #data = response.json()
    response.close()
    #print(data)
    time.sleep(3)
    
    