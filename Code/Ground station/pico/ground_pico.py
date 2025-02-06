
# CanSat Base Station Pico
# Written by Robert Jordan

import digitalio
import board
import busio
import time
import adafruit_rfm9x

class Radio:
    def recive(self):
        return self.rfm9x.receive(timeout=1.0)
    def send(message, self):
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

#retrurns time in a human readable format
def str_time():
    str_time = time.struct_time()
    return "{}:{}:{}".format(str_time[3],str_time[4],str_time[5])

def main():
    print("Ground Station Pico Starting...")

    #turn on onboard led
    led = digitalio.DigitalInOut(board.GP25)
    led.direction = digitalio.Direction.OUTPUT
    led.value = True

    #start radio
    radio = Radio()
    print("Radio Initialised Succesfully!")
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
            print("Time Recived : {}".format(str_time()))

if __name__ == "__main__":
    main()
