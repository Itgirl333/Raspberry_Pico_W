import machine
import utime
import math

pot_pin = machine.ADC(28) # POT-input on the Pico
max_val = math.pow(2,16) - 1 # maximum value unsigned 'short' = 2^16-1

while True:
    pot_val = pot_pin.read_u16() # fetch the digital converted value
    pot_pct = pot_val / max_val  # calculate percentage
    print(str(pot_val) + " -> pct: " + str(pot_pct*100))
    
    if pot_pct == 0:    # avoid division through zero
        utime.sleep(1)
    else:               # set frequency with max. 1/100 second and min. 1 second
        utime.sleep(1/(pot_pct*100))