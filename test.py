import tkinter as tk
import time
import sys
import RPi.GPIO as GPIO
import smbus
import fcntl
from tkinter import *

import debugWindow
import leakTestWindow
from GT1000 import GT1000

I2C_BUS = 1
CHIP00 = 0x38
CHIP01 = 0x39
CHIP02 = 0x3a
CHIP03 = 0x3b
CHIPS = {0x38,0x39,0x3a,0x3b}

# Bank Selects
BANK1 = 21
BANK2 = 20
BANK3 = 16
BANK4 = 7
BANKS = {BANK1,BANK2,BANK3,BANK4}

# GPIO Inputs
EXT_IN_START = 13
EXT_IN_ABORT = 19
EXT_OUT_PASS = 18
EXT_OUT_FAIL = 15
EXT_OUT_INTEST = 23



class Window(Frame):
#  label = tk.Label()

  def __init__(self, master=None):
    print("Starting Window.__init__")
    Frame.__init__(self,master)
    self.master = master

    self.pack(fill=BOTH, expand=1)


    # Try a button
    exitCmd =  Button(self, text="Exit", command=self.clickExitCmd,height=2,width=4)
    exitCmd.place(x=0,y=0)

    updateCmd = Button(self, text="Update", command=self.update)
    updateCmd.place(x=40, y=40)

    # Create a label
    label = tk.Label(root, textvariable=labelTxt)


    # Lay out label
    label.pack()


  def clickExitCmd(self):
    exit()

  def update(self):
    print("Window.update()")
    on, off = ' On ', ' off'
    labelTxt.set("Here")
    print(labelTxt.get())
    my_debug.attributes('-topmost', True)
    my_debug.attributes('-topmost', False)
    #self.label['text'] = on if self.label['text'] == ' On ' else off
    #root.after(200, update)

def inputsLoop(self):
  GT1000.read_inputs()
  self.after(500,GT1000,self.inputsLoop)

GT1000 = GT1000()
# Create the main window
my_leakTest = tk.Tk()
##my_debug = tk.Tk()
root = tk.Tk()


labelTxt = StringVar()
labelTxt.set("Hello World!")


####appDebug = debugWindow.debugWindow(my_debug)
appLeakTest = leakTestWindow.leakTestWindow(my_leakTest)
####my_debug.title("Debug Window")
my_leakTest.title("Leak Test")
####appDebug.GT1000 = GT1000
appLeakTest.GT1000 = GT1000
####appDebug.GT1000LblText.set(GT1000)


#root.geometry("320x200")
my_leakTest.geometry("800x480")
####my_debug.geometry("800x480")
root.geometry("800x480")

# Scheduled updates
####appDebug.periodicUpdate()
appLeakTest.periodicUpdate()

# I2C Bus setup
#bus = smbus.SMBus(I2C_BUS)
#testRead = bus.read_byte_data(CHIP00, 0x00)

# Register events
root.after(200, root.update)
# Run forever!
app = Window(root)
root.title("My GUI")

root.lift()
root.attributes('-topmost', True)
root.after_idle(root.attributes, '-topmost', False)

root.mainloop()

