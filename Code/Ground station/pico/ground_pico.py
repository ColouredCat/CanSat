
# CanSat Base Station Pico
# Written by Robert Jordan

import digitalio
import board
import busio
import time
from cansat_lib import Radio, str_time

def main():
    #wait to ensure laptop has esablished connection
    time.sleep(1)
    print("Ground Station Pico Starting...")

    #turn on onboard led
    led = digitalio.DigitalInOut(board.GP25)
    led.direction = digitalio.Direction.OUTPUT
    led.value = True

    #start radio
    radio = Radio()
    print("Radio Initialised Succesfully!")
    print("Time: {}".format(str_time()))
    print("Begining to recieve radio messages...")

    # start reciving radio data
    while True:
        data = radio.recive()

        #check if any data is recived
        if data is not None:
            #convert data to ascii
            data = str(data, 'ascii')
            print(data)

            #print recived time and signal strength
            print("RSSI : {}".format(radio.rfm9x.rssi))
            print("Time Recived : {}\n".format(str_time()))
        print("No data recieved : {}".format(str_time()))

if __name__ == "__main__":
    main()
