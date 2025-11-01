
import digitalio
import board
import busio
import time
import adafruit_rfm9x
import adafruit_bmp280
import adafruit_mpu6050

class Radio:
    def recive(self):
        #try and revieve, checking the radio is still initialised
        try:
            data = self.rfm9x.receive(timeout=1.0)
            
            #check if any data is recived
            if data is not None:
                #convert data to ascii
                data = str(data, 'ascii')

                #print recived time and signal strength
                print("{} \nRSSI : {}, Uptime {}".format(data, self.rfm9x.rssi, str_time()))
            else:
                print("No data recieved : {}".format(str_time()))
                
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

class BMP:
    def temperature(self):
        #check the sensor is still initialised
        try:
            return self.bmp280.temperature
        except Exception as e:
            self.radio.send("BMP falire!\nThe exception that occured was: {}".format(e))
            return -1

    def pressure(self):
        #check the sensor is still initialised
        try:
            return self.bmp280.pressure
        except Exception as e:
            self.radio.send("BMP falire!\nThe exception that occured was: {}".format(e))
            return -1

    def __init__(self, radio):
        init = False
        self.radio = radio
	    #try to intialise sensor
        while not init:
            try:
                i2c = busio.I2C(scl = board.GP13, sda = board.GP12)
                self.bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, address=0x76)
                init = True
            except Exception as e:
                # retry on error
                self.radio.send("Could not initialise BMP!\nThe exception that occured was: {}".format(e))
                time.sleep(3)

class MPU:
    def __init__(self, radio):
        init = False
        self.radio = radio
        #try to initialise
        while not init:
            try:
                i2c = busio.I2C(scl = board.GP15, sda = board.GP14)
                self.mpu = adafruit_mpu6050.MPU6050(i2c)
                #calibrate the sensor
                self.mpu.accelerometer_range = adafruit_mpu6050.Range.RANGE_2_G
                self.mpu.gyro_range = adafruit_mpu6050.GyroRange.RANGE_250_DPS
                init = True
            except Exception as e:
                # retry on error
                self.radio.send("Could not initialise MPU!\nThe exception that occured was: {}".format(e))
                time.sleep(3)
                
    def reading(self):
        try:
            a = self.mpu.scale_accel(self.mpu.acceleration)
            g = self.mpu.scale_gyro(self.mpu.gyro)
            return "{},{},{},{},{},{}".format(a[0], a[1], a[2], g[0], g[1], g[2])
        except Exception as e:
            self.radio.send("MPU faliure!\nThe exception that occured was: {}".format(e))                

#retrurns time in a human readable format
def str_time():
    return str(time.monotonic())