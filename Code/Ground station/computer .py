
# CanSat Base Station Computer
# Writen by Robert Jordan

import serial
import config
from datetime import datetime
from time import sleep

# define maro for time
def time():
    return datetime.now().strftime("%H:%M:%S")

class Window():

    def loop(self):
        try:
            # if pico has sent data, try to read, diplay and log it
            if self.pico.inWaiting():
                data = self.pico.readline().decode("utf-8")

                # remove pesky control characters!
                data = data.replace("\015", " ")
                data = data.replace("\033", " ")

                print(data)
                self.log.write(str(data))
        except serial.SerialException:
            # print a warning on exception
            print("There was an error reading from the serial.")
            print("Pico may be unplugged or sending corrupt data.")

    def open_serial(self):
        #start serial to pico
        running = True
        while running:
            try:
                self.pico = serial.Serial(config.serial_port)
                #open port if not already open
                #if not self.pico.isOpen():
                    #self.pico.open()
                running = False
            except serial.SerialException:
                # retry if exeption occors
                print("There was an error conecting to the pico.")
                print("Please ensure it is pluged it, and specify the serial path it is conected to using the config file.")
                sleep(0.5)

    def __init__(self):

        #create log file
        try:
            self.log = open("log-"+time(), "w+")
        except OSError:
            print("Error: log file could not be created")
            print("Check write permisions and ensure there is enough disk space.")
            exit()

        self.open_serial()

        running = True
        while running:
            try:
                self.loop()
                sleep(config.tick_speed)
            except KeyboardInterrupt:
                running = False

if __name__ == "__main__":
    win = Window()
    #ensure to close the port after window close
    win.pico.close()
    win.log.close()