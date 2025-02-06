
# CanSat Base Station Computer
# Writen by Robert Jordan

import serial
import tkinter as tk
import config
from datetime import datetime
from time import sleep

# define maro for time
def time():
    return datetime.now().strftime("%H:%M:%S")

class Window(tk.Tk):

    def loop(self):
        try:
            # if pico has sent data, try to read, diplay and log it
            if self.pico.inWaiting():
                data = self.pico.readline().decode("utf-8")

                # remove peskey control characters!
                data = data.replace("\015", " ")
                data = data.replace("\033", " ")

                self.text.insert("end", data)
                self.log.write(str(data))
        except serial.SerialException:
            # output a warning on exception
            self.text.insert("end", "There was an error reading from the serial\n")
            self.text.insert("end", "Pico may be unplugged or sending corrupt data.\n")

        #repeat every tick_speed ms
        self.after(config.tick_speed, self.loop)

    def window_setup(self):
        super().__init__()
        self.title(config.win_name) 

        tk.Label(self,text="CanSat Ground Station Reciver").pack()
        tk.Label(self,text="Reciving data from port " + config.serial_port).pack()

        scrollbar = tk.Scrollbar(self) 
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y) 
    
        self.text = tk.Text(self, width =config.text_width
                    , height=config.text_height) 
        self.text.pack(fill=tk.BOTH) 
        scrollbar.config(command=self.text.yview) 

    def open_serial(self):
        #start serial to pico
        running = True
        while running:
            try:
                self.pico = serial.Serial(config.serial_port)
                #open port if not already open
                if not self.pico.isOpen():
                    self.pico.open()
                running = False
            except serial.SerialException:
                # retry if exeption occors
                print("There was an error conecting to the pico.")
                print("Please ensure it is pluged it, and specify the serial path it is conected to using the config file.")
                sleep(0.5)

    def __init__(self):

        self.window_setup()

        #create log file
        try:
            self.log = open("log-"+time(), "w+")
        except OSError:
            print("Error: log file could not be created")
            print("Check write permisions and ensure there is enough disk space.")
            exit()

        self.open_serial()

        # start mainloop
        self.loop()
        self.mainloop()

if __name__ == "__main__":
    win = Window()
    #ensure to close the port after window close
    win.pico.close()
    win.log.close()