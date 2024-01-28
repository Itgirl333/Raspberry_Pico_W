import machine
from machine import Pin
import utime
from time import sleep
import network
import urequests

ssid = "YOUR_SSID"
password = 'YOUR_PASSWORD'

IFTTT_API_KEY = "YOUR_IFTTT_API_KEY"
IFTT_GOOGLE_EVENT = "YOUR_IFTT_GOOGLE_EVENT"
IFTTT_LINE_EVENT = "YOUR_IFTTT_LINE_EVENT"
IFTTT_URL_GOOGLE_SHEET = 'https://maker.ifttt.com/trigger/' + IFTT_GOOGLE_EVENT +'/with/key/' + IFTTT_API_KEY
IFTTT_URL_LINE = 'https://maker.ifttt.com/trigger/' + IFTTT_LINE_EVENT +'/with/key/' + IFTTT_API_KEY

trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)

def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')

def get_ultrasonic():
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(5)
    trigger.low()
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.ticks_us()
    timepassed = signalon - signaloff
    distance = (timepassed * 0.0343) / 2
    return distance

def send_to_ifttt(url, data, state):
    data = {'value1': data, 'value2': state}
    print(data)
    request_headers = {'Content-Type': 'application/json'}
    request = urequests.post(url, json=data, headers=request_headers)
    print(request.text)
    request.close()

try:
    connect()
    while True:
        distance = round(get_ultrasonic(), 2)
        if distance < 5.0:
            state = 'ALERT!'
            send_to_ifttt(IFTTT_URL_LINE, distance, state)
        else:
            state = 'Normal'
        send_to_ifttt(IFTTT_URL_GOOGLE_SHEET, distance, state)
        utime.sleep(1)
except KeyboardInterrupt:
    machine.reset()


