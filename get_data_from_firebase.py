import network
import urequests
import time

ssid = "YOUR_SSID"
password = 'YOUR_PASSWORD'

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
print(auth_response_data)
auth_response.close()
local_id = auth_response_data.get('localId')
print(local_id)

response = urequests.get(firebase_url)
data = response.json()
response.close()
print(data)