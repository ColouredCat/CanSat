# radio.py
# Select the radio connection
import busio
import board
import digitalio 
import adafruit_rfm9x

def radio_433():
    spi = busio.SPI(clock=board.GP2, MOSI=board.GP3, MISO=board.GP4)
    cs = digitalio.DigitalInOut(board.GP6)
    reset = digitalio.DigitalInOut(board.GP7)

    print("\n Radio module called")

    rfm9x_433 = adafruit_rfm9x.RFM9x(spi, cs, reset, 433.0)
    print("\nRadio ready")
    return rfm9x_433

def radio_900():
    spi = busio.SPI(clock=board.GP18, MOSI=board.GP19, MISO=board.GP16)
    cs = digitalio.DigitalInOut(board.GP8)
    reset = digitalio.DigitalInOut(board.GP9)

    print("\n Radio module called")

    rfm9x_900 = adafruit_rfm9x.RFM9x(spi, cs, reset, 863.0)
    print("Radio ready")
    return rfm9x_900

def send(rfm, message):
    rfm.send(message)
    
def read(rfm, stime = 1.0):
    return rfm.receive(timeout=stime)

def rssi():
    return rfm9x.rssi