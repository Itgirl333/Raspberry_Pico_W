import ble_uart_v7rc
import bluetooth
from machine import Pin

led = Pin(16, Pin.OUT)

def rx_callback():
  b = uart.read()  
  s = b.decode('utf-8').strip().lower()
  print(s)
  if s == 'on':
      led.value(True)
  if s =='off':
      led.value(False)

ble = bluetooth.BLE()
uart = ble_uart_v7rc.ble_uart(ble, rx_callback=rx_callback, name="pico_ble")

