
# Main CanSat Code
# Written by Robert Jordan

import digitalio
import board
import time
from cansat_lib import Radio, Sensor, str_time

def main():
    time.sleep(1)
    print("CanSat Starting...")

    #turn on onboard led
    led = digitalio.DigitalInOut(board.GP25)
    led.direction = digitalio.Direction.OUTPUT
    led.value = True

    # initailise modules
    radio = Radio()
    radio.send("Radio Module Initialised!")
    sensor = Sensor(radio)
    radio.send("Sensor Module Initialised!")

    # start mainloop
    radio.send("Hello from CanSat!\nBegiooing Transmuion...")

    while True:
        # send report on temp and pressure
        tme = str_time()
        tmp = sensor.temperature()
        prs = sensor.pressure()
        msg = "Sent : {} \nTemperature : {} \nPressure : {}".format(tme, tmp, prs)
        radio.send(msg)
        time.sleep(1)


if __name__ == "__main__":
    main()
