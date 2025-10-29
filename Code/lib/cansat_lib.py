
import digitalio
import board
import busio
import time
import adafruit_rfm9x
import adafruit_bmp280

class Radio:
    def recive(self):
        #try and revieve, checking the radio is still initialised
        try:
            self.rfm9x.receive(timeout=1.0)
        except Exception as e:
            print("Radio falire!\nThe exception that occred was: {}".format(e))

    def send(self, message):
        # append the signiture of the CanSat
        message = "CVC-CANSAT:" + message
        #radio can't send over 255 bytes, so limit the message at that
        if len(message) > 255:
            print("Message too large! Cutting it short at 255 bytes...")
            l = list(message)[0:255]
            message = str(l)

        print(message)
        #try and send the message, checking the radio is still initialised
        try:
            self.rfm9x.send(message)
        except Exception as e:
            print("Radio falire!\nThe exception that occred was: {}".format(e))

    def __init__(self):
        init = False
	
	    #try to intialise radio
        while not init:
            try:
                #setup all pins
                spi = busio.SPI(clock=board.GP2, MOSI=board.GP3, MISO=board.GP4)
                cs = digitalio.DigitalInOut(board.GP6)
                reset = digitalio.DigitalInOut(board.GP7)
                self.rfm9x = adafruit_rfm9x.RFM9x(spi, cs, reset, 433.0)
                init = True
            except Exception as e:
                # retry on error
                print("Could not initialise radio module!\nThe exception that occured was: {}".format(e))
                time.sleep(3)

class Sensor:
    def temperature(self):
        #check the sensor is still initialised
        try:
            return self.bmp280.temperature
        except Exception as e:
            self.radio.send("Sensor falire!\nThe exception that occored was: {}".format(e))
            return -1

    def pressure(self):
        #check the sensor is still initialised
        try:
            return self.bmp280.pressure
        except Exception as e:
            self.radio.send("Sensor falire!\nThe exception that occored was: {}".format(e))
            return -1

    def __init__(self, radio):
        init = False
        self.radio = radio
	    #try to intialise sensor
        while not init:
            try:
                i2c = busio.I2C(scl = board.GP15, sda = board.GP14)
                self.bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, address=0x76)
                init = True
            except Exception as e:
                # retry on error
                self.radio.send("Could not initialise sensor module!\nThe exception that occured was: {}".format(e))
                time.sleep(3)


#retrurns time in a human readable format
def str_time():
    return str(time.monotonic())
