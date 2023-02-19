import tkinter as tk
from tkinter import *
from GT1000 import GT1000

class leakTestWindow(Frame):

  #def periodicUpdate(self):
  #  print("[call] periodicUpdate()")
  #  self.update
  def __init__(self, master=None):
    print("<NEW> Initializing leakTestWindow")
    Frame.__init__(self,master)
    self.pack(fill=BOTH, expand=1)

    self.GT1000 = GT1000()
    self.testPart = "Nothing"

    self.station01Text = StringVar()
    self.station02Text = StringVar()
    self.station03Text = StringVar()
    self.station04Text = StringVar()
    self.station05Text = StringVar()
    self.station06Text = StringVar()
    self.station07Text = StringVar()
    self.station08Text = StringVar()
    self.station09Text = StringVar()
    self.station10Text = StringVar()
    self.station11Text = StringVar()
    self.station12Text = StringVar()
    self.station13Text = StringVar()
    self.station14Text = StringVar()
    self.station15Text = StringVar()
    self.station16Text = StringVar()
    self.station17Text = StringVar()
    self.station18Text = StringVar()
    self.station19Text = StringVar()
    self.station20Text = StringVar()

    self.station01Text.set("Station 1")
    self.station02Text.set("Station 2")
    self.station03Text.set("Station 3")
    self.station04Text.set("Station 4")
    self.station05Text.set("Station 5")
    self.station06Text.set("Station 6")
    self.station07Text.set("Station 7")
    self.station08Text.set("Station 8")
    self.station09Text.set("Station 9")
    self.station10Text.set("Station 10")
    self.station11Text.set("Station 11")
    self.station12Text.set("Station 12")
    self.station13Text.set("Station 13")
    self.station14Text.set("Station 14")
    self.station15Text.set("Station 15")
    self.station16Text.set("Load H4568")
    self.station17Text.set("Load H4569")
    self.station18Text.set("Test All")
    self.station19Text.set("Reset")
    self.station20Text.set("")

    self.station01Cmd = Button(self,textvariable=self.station01Text,command=self.station01Cmd__click,height=6,width=16)
    self.station01Cmd.grid(row=0,column=0,sticky='nsew')
    self.station02Cmd = Button(self,textvariable=self.station02Text,command=self.station02Cmd__click,width=16)
    self.station02Cmd.grid(row=0,column=1,sticky='nsew')
    self.station03Cmd = Button(self,textvariable=self.station03Text,command=self.station03Cmd__click,width=16)
    self.station03Cmd.grid(row=0,column=2,sticky='nsew')
    self.station04Cmd = Button(self,textvariable=self.station04Text,command=self.station04Cmd__click,width=16)
    self.station04Cmd.grid(row=0,column=3,sticky='nsew')
    self.station05Cmd = Button(self,textvariable=self.station05Text,command=self.station05Cmd__click,width=16)
    self.station05Cmd.grid(row=0,column=4,sticky='nsew')
    self.station06Cmd = Button(self,textvariable=self.station06Text,command=self.station06Cmd__click,height=6,)
    self.station06Cmd.grid(row=1,column=0,sticky='nsew')
    self.station07Cmd = Button(self,textvariable=self.station07Text,command=self.station07Cmd__click)
    self.station07Cmd.grid(row=1,column=1,sticky='nsew')
    self.station08Cmd = Button(self,textvariable=self.station08Text,command=self.station08Cmd__click)
    self.station08Cmd.grid(row=1,column=2,sticky='nsew')
    self.station09Cmd = Button(self,textvariable=self.station09Text,command=self.station09Cmd__click)
    self.station09Cmd.grid(row=1,column=3,sticky='nsew')
    self.station10Cmd = Button(self,textvariable=self.station10Text,command=self.station10Cmd__click)
    self.station10Cmd.grid(row=1,column=4,sticky='nsew')
    self.station11Cmd = Button(self,textvariable=self.station11Text,command=self.station11Cmd__click,height=6)
    self.station11Cmd.grid(row=2,column=0,sticky='nsew')
    self.station12Cmd = Button(self,textvariable=self.station12Text,command=self.station12Cmd__click)
    self.station12Cmd.grid(row=2,column=1,sticky='nsew')
    self.station13Cmd = Button(self,textvariable=self.station13Text,command=self.station13Cmd__click)
    self.station13Cmd.grid(row=2,column=2,sticky='nsew')
    self.station14Cmd = Button(self,textvariable=self.station14Text,command=self.station14Cmd__click)
    self.station14Cmd.grid(row=2,column=3,sticky='nsew')
    self.station15Cmd = Button(self,textvariable=self.station15Text,command=self.station15Cmd__click)
    self.station15Cmd.grid(row=2,column=4,sticky='nsew')
    self.station16Cmd = Button(self,textvariable=self.station16Text,command=self.station16Cmd__click,height=6,bg="yellow")
    self.station16Cmd.grid(row=3,column=0,sticky='nsew')
    self.station17Cmd = Button(self,textvariable=self.station17Text,command=self.station17Cmd__click,bg="white")
    self.station17Cmd.grid(row=3,column=1,sticky='nsew')
    self.station18Cmd = Button(self,textvariable=self.station18Text,command=self.station18Cmd__click,bg="cyan")
    self.station18Cmd.grid(row=3,column=2,sticky='nsew')
    self.station19Cmd = Button(self,textvariable=self.station19Text,command=self.station19Cmd__click,fg="white",bg="black")
    self.station19Cmd.grid(row=3,column=3,sticky='nsew')
    self.station20Cmd = Button(self,textvariable=self.station20Text,command=self.station20Cmd__click)
    self.station20Cmd.grid(row=3,column=4,sticky='nsew')
    self.resetButtonColours()


  def station01Cmd__click(self):
    print("1")
  def station02Cmd__click(self):
    print("2")
  def station03Cmd__click(self):
    print("3")
  def station04Cmd__click(self):
    print("4")
  def station05Cmd__click(self):
    print("5")
  def station06Cmd__click(self):
    print("6")
  def station07Cmd__click(self):
    print("7")
  def station08Cmd__click(self):
    print("8")
  def station09Cmd__click(self):
    print("9")
  def station10Cmd__click(self):
    print("10")
  def station11Cmd__click(self):
    print("11")
  def station12Cmd__click(self):
    print("12")
  def station13Cmd__click(self):
    print("13")
  def station14Cmd__click(self):
    print("14")
  def station15Cmd__click(self):
    print("15")
  def station16Cmd__click(self):
    print("<LOAD 4568>")
    self.testPart = "4568"
    self.station01Text.set("Test ACM 1")
    self.station02Text.set("Test AFB 1")
    self.station03Text.set("Test LED_L")
    self.station04Text.set("Test LED_R")
    self.station05Text.set("Test DLC 2")
    self.station06Text.set("Test KEY_PAD")
    self.station07Text.set("Test WIPER")
    self.station08Text.set("Test DLC 1")
    self.station09Text.set("Test WASHER")
    self.station10Text.set("Test PWR_FLIP")
    self.station11Text.set("Test SNS 1")
    self.station12Text.set("Test LED_BUMPER")
    self.station13Text.set("Test LED_ROOF")
    self.station14Text.set("Test LED_HOOD")
    self.station15Text.set("")

  def station17Cmd__click(self):
    print("<LOAD 4569>")
    self.testPart = "4569"
    self.station01Text.set("Test ACM 2")
    self.station02Text.set("Test AFB 2")
    self.station03Text.set("Test HELMET_FAN")
    self.station04Text.set("Test PARTICULE")
    self.station05Text.set("Test LED_CHASE_1")
    self.station06Text.set("Test LED_CHASE_2")
    self.station07Text.set("Test LED_CHASE_3")
    self.station08Text.set("")
    self.station09Text.set("")
    self.station10Text.set("")
    self.station11Text.set("")
    self.station12Text.set("")
    self.station13Text.set("")
    self.station14Text.set("")
    self.station15Text.set("")

  def station18Cmd__click(self):
    print("<TEST ALL>")
  def station19Cmd__click(self):
    print("<RESET>")
    self.resetButtonColours()
    self.station01Cmd["bg"]="grey90"
    self.station02Cmd["bg"]="grey90"
    self.station03Cmd["bg"]="grey90"
    self.station04Cmd["bg"]="grey90"
    self.station05Cmd["bg"]="grey90"
    self.station06Cmd["bg"]="grey90"
    self.station07Cmd["bg"]="grey90"
    self.station08Cmd["bg"]="grey90"
    self.station09Cmd["bg"]="grey90"
    self.station10Cmd["bg"]="grey90"
    self.station11Cmd["bg"]="grey90"
    self.station12Cmd["bg"]="grey90"
    self.station13Cmd["bg"]="grey90"
    self.station14Cmd["bg"]="grey90"
    self.station15Cmd["bg"]="grey90"
  def station20Cmd__click(self):
    print("<NOTHING>")


  def resetButtonColours(self):
    print("resetButtonColours()")
#    self.station01Cmd.configure(bg="grey")
