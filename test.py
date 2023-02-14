import tkinter as tk
import time
import sys
import RPi.GPIO as GPIO
import smbus
import fcntl
from tkinter import *

I2C_BUS = 1
CHIP00 = 0x38
CHIP01 = 0x39
CHIP02 = 0x3a
CHIP03 = 0x3b
CHIPS = {0x38,0x39,0x3a,0x3b}

class Window(Frame):
  def __init__(self, master=None):
    Frame.__init__(self,master)
    self.master = master

    self.pack(fill=BOTH, expand=1)

    # Try a button
    exitCmd =  Button(self, text="Exit", command=self.clickExitCmd)
    exitCmd.place(x=0,y=0)

    # Create a label
    label = tk.Label(root, text="Hello World!")


    # Lay out label
    label.pack()


  def clickExitCmd(self):
    exit()

# Create the main window
root = tk.Tk()
app = Window(root)
root.title("My GUI")
#root.geometry("320x200")
root.geometry("800x480")

# I2C Bus setup
bus = smbus.SMBus(I2C_BUS)
testRead = bus.read_byte_data(CHIP00, 0x00)

# Run forever!
root.mainloop()

