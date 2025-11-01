
# Main CanSat Code
# Written by Robert Jordan

import digitalio
import board
import time
from cansat_lib import Radio, BMP, str_time, MPU

def main():
    print("CanSat Starting...")

    #turn on onboard led
    led = digitalio.DigitalInOut(board.GP25)
    led.direction = digitalio.Direction.OUTPUT
    led.value = True

    # initailise modules
    radio = Radio()
    radio.send("Radio Module Initialised!")
    BMP_sensor = BMP(radio)
    radio.send("BMP Module Initialised!")
    MPU_sensor = MPU(radio)
    radio.send("MPU Module Initialised!")

    radio.send("Starting data transmition...")

    while True:
        # send report on temp and pressure
        tme = str_time()
        tmp = BMP_sensor.temperature()
        prs = BMP_sensor.pressure()
        msg = "{},{},{},".format(tme, tmp, prs)
        msg += MPU_sensor.reading()
        radio.send(msg)
        time.sleep(0.5)


if __name__ == "__main__":
    main()
