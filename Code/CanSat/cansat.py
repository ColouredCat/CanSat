
# Main CanSat Code
# Written by Robert Jordan

import digitalio
import board
import busio
import time
import adafruit_rfm9x
import adafruit_bmp280

class Radio:
    def send(message, self):
        print(message)
        self.rfm9x.send(message)
    def __init__(self):
        #setup variables
        spi = busio.SPI(clock=board.GP2, MOSI=board.GP3, MISO=board.GP4)
        cs = digitalio.DigitalInOut(board.GP6)
        reset = digitalio.DigitalInOut(board.GP7)
        init = False
	
	    #try to intialise radio
        while not init:
            try:
                self.rfm9x = adafruit_rfm9x.RFM9x(spi, cs, reset, 433.0)
                init = True
            except RuntimeError:
                # retry on error
                print("Could not initialise radio module.")
                print("Check wiring and try again")
                time.sleep(3)

class Sensor:
    def temperature(self):
        return self.bmp280.temperature
    def pressure(self):
        return self.bmp280.pressure
    def __init__(self, radio):
        init = False
	    #try to intialise sensor
        while not init:
            try:
                i2c = busio.I2C(scl = board.GP15, sda = board.GP14)
                self.bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, address=0x76)
                init = True
            except RuntimeError:
                # retry on error
                radio.send("Could not initialise sensor module.")
                radio.send("Check wiring and try again")
                time.sleep(3)

#retrurns time in a human readable format
def str_time():
    str_time = time.struct_time()
    return "{}:{}:{}".format(str_time[3],str_time[4],str_time[5])

def main():
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
    radio.send("Hello from CanSat!")
    radio.send("Begining Transmition...")

    while True:
        # send report on temp and pressure
        time = str_time()
        tmp = sensor.temperature()
        prs = sensor.pressure()
        msg = "Sent : {} \nTemperature : {} \nPressure : {}\n".format(time, tmp, prs)
        radio.send(msg)


if __name__ == "__main__":
    main()
