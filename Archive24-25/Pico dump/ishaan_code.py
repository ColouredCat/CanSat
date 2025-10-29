import digitalio
import board
import radio
import time
import bmp280

x = True


while x == True:
    time.sleep(0.5)
    x = False
    time.sleep(0.5)
    x = True
    message = "Temp : " + str(bmp280.read_temperature()) + '\n' " Pressure : " + str(bmp280.read_pressure()) + '\n'
    radio.send(message)



