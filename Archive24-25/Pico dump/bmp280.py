import board
import busio
import adafruit_bmp280

i2c = busio.I2C(sda = board.GP14, scl = board.GP15)
bmp280_sensor = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, address=0x76)

def read_temperature():
    return bmp280_sensor.temperature

def read_pressure():
    return bmp280_sensor.pressure


