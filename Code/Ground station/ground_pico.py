
# CanSat Base Station Pico
# Written by Robert Jordan

import digitalio
import board
import busio
import time
from cansat_lib import Radio, str_time

def main():
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
        radio.recive()

if __name__ == "__main__":
    main()

