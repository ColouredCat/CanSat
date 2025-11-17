import digitalio
import board
import busio
import adafruit_rfm9x
import time



spi = busio.SPI(clock=board.GP2, MOSI=board.GP3, MISO=board.GP4)
cs = digitalio.DigitalInOut(board.GP6)
reset = digitalio.DigitalInOut(board.GP7)
time.sleep(2)
rfm9x = adafruit_rfm9x.RFM9x(spi, cs, reset, 433.0)


print("RFM9x radio ready")

def send(message):
    rfm9x.send(message)



