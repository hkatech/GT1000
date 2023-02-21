import tkinter as tk
from tkinter import *
from GT1000 import GT1000
import time

class leakTestWindow(Frame):

  #def periodicUpdate(self):
  #  print("[call] periodicUpdate()")
  #  self.update
  def periodicUpdate(self):
    print("--- Periodic Call ---")
    self.updateInputs()

    # This section manually releases the latches after 5seconds
    try:
      if not self.GT1000.GT_Abort:
        self.lastAbortTick = time.time()
    except Exception as e:
      pass
    if (time.time() - self.lastAbortTick) > 5:
      if not self.GT1000.getLatchState():
        self.GT1000.latchReleaseEn()
    elif self.GT1000.getLatchState():
      self.GT1000.latchReleaseDis()

    # Update part number based on selector switch
    if self.testPart == "4568":
      if self.GT1000.GT_PartSelect:
        self.station17Cmd__click()
    elif self.testPart == "4569":
      if not self.GT1000.GT_PartSelect:
        self.station16Cmd__click()
    else:
      self.station17Cmd__click()

    # Handle the start push
    if self.GT1000.GT_Start:
      self.station18Cmd__click()

    self.after(500,self.periodicUpdate)

  def updateInputs(self):
    self.GT1000.read_inputs()

  def resetResults(self):
    for val in self.stationResults:
      val = ""

  def __init__(self, master=None):
    print("<NEW> Initializing leakTestWindow")
    Frame.__init__(self,master)
    self.pack(fill=BOTH, expand=1)

    self.GT1000 = GT1000()
    self.testPart = "Nothing"
    self.abortSignal = False
    self.testingAll = False

    self.station01Result = StringVar()
    self.station02Result = StringVar()
    self.station03Result = StringVar()
    self.station04Result = StringVar()
    self.station05Result = StringVar()
    self.station06Result = StringVar()
    self.station07Result = StringVar()
    self.station08Result = StringVar()
    self.station09Result = StringVar()
    self.station10Result = StringVar()
    self.station11Result = StringVar()
    self.station12Result = StringVar()
    self.station13Result = StringVar()
    self.station14Result = StringVar()
    self.station15Result = StringVar()
    self.station16Result = StringVar()
    self.station17Result = StringVar()
    self.station18Result = StringVar()
    self.station19Result = StringVar()
    self.station20Result = StringVar()
    self.stationResults = [StringVar()] * 20
    self.resetResults()

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
    self.stationTexts = [StringVar()] * 20

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

# TODO: Add case checks for blank stations and ignore

  def station01Cmd__click(self):
    print("1")
    s = self.station01Text.get()
    self.GT1000.enableStations([1])
    self.station01Cmd["bg"] = "yellow"
    self.station01Cmd["activebackground"] = "yellow"
    self.station01Text.set(s + "\nIn Test")
    self.update()
    if self.GT1000.startTest() >= 1:
      while self.GT1000.GT_InTest:
        print("Waiting on station 1...", self.GT1000.GT_InTest)
        self.GT1000.read_inputs()
        if self.GT1000.GT_Abort:
          print("{Test Abort}")
          self.station01Cmd["bg"] = "red"
          self.station01Text.set(s + "\nTest Aborted")
          return
        if self.GT1000.GT_Fail:
          print("{Test FAILED}")
          self.station01Cmd["bg"] = "red"
          self.station01Text.set(s + "\nTest FAILED")
          return
        if self.GT1000.GT_Pass:
          print("{Test PASSED}")
          self.station01Cmd["bg"] = "green"
          self.station01Text.set(s +"\n << PASSED >>")
          return
      self.station01Cmd["bg"] = "red"
      self.station01Cmd["activebackground"] = self.station01Cmd["bg"]
      self.station01Text.set(s + "\nAbnormal Completion")
  def station02Cmd__click(self):
    print("2")
    s = self.station02Text.get()
    if self.testPart == "4568":
      self.GT1000.enableStations([2])
    else:
      self.GT1000.enableStations([3])
    self.station02Cmd["bg"] = "yellow"
    self.station02Cmd["activebackground"] = "yellow"
    self.station02Text.set(s + "\nIn Test")
    self.update()
    if self.GT1000.startTest() >= 1:
      while self.GT1000.GT_InTest:
        self.GT1000.read_inputs()
        if self.GT1000.GT_Abort:
          print("{Test Abort}")
          self.station02Cmd["bg"] = "red"
          self.station02Text.set(s + "\nTest Aborted")
          return
        if self.GT1000.GT_Fail:
          print("{Test FAILED}")
          self.station02Cmd["bg"] = "red"
          self.station02Text.set(s + "\nTest FAILED")
          return
        if self.GT1000.GT_Pass:
          print("{Test PASSED}")
          self.station02Cmd["bg"] = "green"
          self.station02Text.set(s +"\n << PASSED >>")
          return
      self.station02Cmd["bg"] = "red"
      self.station02Cmd["activebackground"] = self.station02Cmd["bg"]
      self.station02Text.set(s + "\nAbnormal Completion")
  def station03Cmd__click(self):
    print("3")
    s = self.station03Text.get()
    self.GT1000.enableStations([4])
    self.station03Cmd["bg"] = "yellow"
    self.station03Cmd["activebackground"] = "yellow"
    self.station03Text.set(s + "\nIn Test")
    self.update()
    if self.GT1000.startTest() >= 1:
      while self.GT1000.GT_InTest:
        self.GT1000.read_inputs()
        if self.GT1000.GT_Abort:
          print("{Test Abort}")
          self.station03Cmd["bg"] = "red"
          self.station03Text.set(s + "\nTest Aborted")
          return
        if self.GT1000.GT_Fail:
          print("{Test FAILED}")
          self.station03Cmd["bg"] = "red"
          self.station03Text.set(s + "\nTest FAILED")
          return
        if self.GT1000.GT_Pass:
          print("{Test PASSED}")
          self.station03Cmd["bg"] = "green"
          self.station03Text.set(s +"\n << PASSED >>")
          return
      self.station03Cmd["bg"] = "red"
      self.station03Cmd["activebackground"] = self.station03Cmd["bg"]
      self.station03Text.set(s + "\nAbnormal Completion")
  def station04Cmd__click(self):
    print("4")
    s = self.station04Text.get()
    self.GT1000.enableStations([5])
    self.station04Cmd["bg"] = "yellow"
    self.station04Cmd["activebackground"] = "yellow"
    self.station04Text.set(s + "\nIn Test")
    self.update()
    if self.GT1000.startTest() >= 1:
      while self.GT1000.GT_InTest:
        self.GT1000.read_inputs()
        if self.GT1000.GT_Abort:
          print("{Test Abort}")
          self.station04Cmd["bg"] = "red"
          self.station04Text.set(s + "\nTest Aborted")
          return
        if self.GT1000.GT_Fail:
          print("{Test FAILED}")
          self.station04Cmd["bg"] = "red"
          self.station04Text.set(s + "\nTest FAILED")
          return
        if self.GT1000.GT_Pass:
          print("{Test PASSED}")
          self.station04Cmd["bg"] = "green"
          self.station04Text.set(s +"\n << PASSED >>")
          return
      self.station04Cmd["bg"] = "red"
      self.station04Cmd["activebackground"] = self.station04Cmd["bg"]
      self.station04Text.set(s + "\nAbnormal Completion")
  def station05Cmd__click(self):
    print("5")
    s = self.station05Text.get()
    self.GT1000.enableStations([6])
    self.station05Cmd["bg"] = "yellow"
    self.station05Cmd["activebackground"] = "yellow"
    self.station05Text.set(s + "\nIn Test")
    self.update()
    if self.GT1000.startTest() >= 1:
      while self.GT1000.GT_InTest:
        self.GT1000.read_inputs()
        if self.GT1000.GT_Abort:
          print("{Test Abort}")
          self.station05Cmd["bg"] = "red"
          self.station05Text.set(s + "\nTest Aborted")
          return
        if self.GT1000.GT_Fail:
          print("{Test FAILED}")
          self.station05Cmd["bg"] = "red"
          self.station05Text.set(s + "\nTest FAILED")
          return
        if self.GT1000.GT_Pass:
          print("{Test PASSED}")
          self.station05Cmd["bg"] = "green"
          self.station05Text.set(s +"\n << PASSED >>")
          return
      self.station05Cmd["bg"] = "red"
      self.station05Cmd["activebackground"] = self.station05Cmd["bg"]
      self.station05Text.set(s + "\nAbnormal Completion")
  def station06Cmd__click(self):
    print("6")
    s = self.station06Text.get()
    self.GT1000.enableStations([7])
    self.station06Cmd["bg"] = "yellow"
    self.station06Cmd["activebackground"] = "yellow"
    self.station06Text.set(s + "\nIn Test")
    self.update()
    if self.GT1000.startTest() >= 1:
      while self.GT1000.GT_InTest:
        self.GT1000.read_inputs()
        if self.GT1000.GT_Abort:
          print("{Test Abort}")
          self.station06Cmd["bg"] = "red"
          self.station06Text.set(s + "\nTest Aborted")
          return
        if self.GT1000.GT_Fail:
          print("{Test FAILED}")
          self.station06Cmd["bg"] = "red"
          self.station06Text.set(s + "\nTest FAILED")
          return
        if self.GT1000.GT_Pass:
          print("{Test PASSED}")
          self.station06Cmd["bg"] = "green"
          self.station06Text.set(s +"\n << PASSED >>")
          return
      self.station06Cmd["bg"] = "red"
      self.station06Cmd["activebackground"] = self.station06Cmd["bg"]
      self.station06Text.set(s + "\nAbnormal Completion")
  def station07Cmd__click(self):
    print("7")
    s = self.station07Text.get()
    if self.testPart == "4568":
      self.GT1000.enableStations([8])
    else:
      self.GT1000.enableStations([9])
    self.station07Cmd["bg"] = "yellow"
    self.station07Cmd["activebackground"] = "yellow"
    self.station07Text.set(s + "\nIn Test")
    self.update()
    if self.GT1000.startTest() >= 1:
      while self.GT1000.GT_InTest:
        self.GT1000.read_inputs()
        if self.GT1000.GT_Abort:
          print("{Test Abort}")
          self.station07Cmd["bg"] = "red"
          self.station07Text.set(s + "\nTest Aborted")
          return
        if self.GT1000.GT_Fail:
          print("{Test FAILED}")
          self.station07Cmd["bg"] = "red"
          self.station07Text.set(s + "\nTest FAILED")
          return
        if self.GT1000.GT_Pass:
          print("{Test PASSED}")
          self.station07Cmd["bg"] = "green"
          self.station07Text.set(s +"\n << PASSED >>")
          return
      self.station07Cmd["bg"] = "red"
      self.station07Cmd["activebackground"] = self.station07Cmd["bg"]
      self.station07Text.set(s + "\nAbnormal Completion")
  def station08Cmd__click(self):
    print("8")
    if self.testPart == "4569":
      self.station08Cmd["bg"] = "green"
      self.station08Cmd["activebackground"] = "green"
      return
    s = self.station08Text.get()
    self.GT1000.enableStations([10])
    self.station08Cmd["bg"] = "yellow"
    self.station08Cmd["activebackground"] = "yellow"
    self.station08Text.set(s + "\nIn Test")
    self.update()
    if self.GT1000.startTest() >= 1:
      while self.GT1000.GT_InTest:
        self.GT1000.read_inputs()
        if self.GT1000.GT_Abort:
          print("{Test Abort}")
          self.station08Cmd["bg"] = "red"
          self.station08Text.set(s + "\nTest Aborted")
          return
        if self.GT1000.GT_Fail:
          print("{Test FAILED}")
          self.station08Cmd["bg"] = "red"
          self.station08Text.set(s + "\nTest FAILED")
          return
        if self.GT1000.GT_Pass:
          print("{Test PASSED}")
          self.station08Cmd["bg"] = "green"
          self.station08Text.set(s +"\n << PASSED >>")
          return
      self.station08Cmd["bg"] = "red"
      self.station08Cmd["activebackground"] = self.station08Cmd["bg"]
      self.station08Text.set(s + "\nAbnormal Completion")
  def station09Cmd__click(self):
    print("9")
    if self.testPart == "4569":
      self.station09Cmd["bg"] = "green"
      self.station09Cmd["activebackground"] = "green"
      return
    s = self.station09Text.get()
    self.GT1000.enableStations([11])
    self.station09Cmd["bg"] = "yellow"
    self.station09Cmd["activebackground"] = "yellow"
    self.station09Text.set(s + "\nIn Test")
    self.update()
    if self.GT1000.startTest() >= 1:
      while self.GT1000.GT_InTest:
        self.GT1000.read_inputs()
        if self.GT1000.GT_Abort:
          print("{Test Abort}")
          self.station09Cmd["bg"] = "red"
          self.station09Text.set(s + "\nTest Aborted")
          return
        if self.GT1000.GT_Fail:
          print("{Test FAILED}")
          self.station09Cmd["bg"] = "red"
          self.station09Text.set(s + "\nTest FAILED")
          return
        if self.GT1000.GT_Pass:
          print("{Test PASSED}")
          self.station09Cmd["bg"] = "green"
          self.station09Text.set(s +"\n << PASSED >>")
          return
      self.station09Cmd["bg"] = "red"
      self.station09Cmd["activebackground"] = self.station09Cmd["bg"]
      self.station09Text.set(s + "\nAbnormal Completion")
  def station10Cmd__click(self):
    print("10")
    if self.testPart == "4569":
      self.station10Cmd["bg"] = "green"
      self.station10Cmd["activebackground"] = "green"
      return
    s = self.station10Text.get()
    self.GT1000.enableStations([12])
    self.station10Cmd["bg"] = "yellow"
    self.station10Cmd["activebackground"] = "yellow"
    self.station10Text.set(s + "\nIn Test")
    self.update()
    if self.GT1000.startTest() >= 1:
      while self.GT1000.GT_InTest:
        self.GT1000.read_inputs()
        if self.GT1000.GT_Abort:
          print("{Test Abort}")
          self.station10Cmd["bg"] = "red"
          self.station10Text.set(s + "\nTest Aborted")
          return
        if self.GT1000.GT_Fail:
          print("{Test FAILED}")
          self.station10Cmd["bg"] = "red"
          self.station10Text.set(s + "\nTest FAILED")
          return
        if self.GT1000.GT_Pass:
          print("{Test PASSED}")
          self.station10Cmd["bg"] = "green"
          self.station10Text.set(s +"\n << PASSED >>")
          return
      self.station10Cmd["bg"] = "red"
      self.station10Cmd["activebackground"] = self.station10Cmd["bg"]
      self.station10Text.set(s + "\nAbnormal Completion")
  def station11Cmd__click(self):
    print("11")
    if self.testPart == "4569":
      self.station11Cmd["bg"] = "green"
      self.station11Cmd["activebackground"] = "green"
      return
    s = self.station11Text.get()
    self.GT1000.enableStations([13])
    self.station11Cmd["bg"] = "yellow"
    self.station11Cmd["activebackground"] = "yellow"
    self.station11Text.set(s + "\nIn Test")
    self.update()
    if self.GT1000.startTest() >= 1:
      while self.GT1000.GT_InTest:
        self.GT1000.read_inputs()
        if self.GT1000.GT_Abort:
          print("{Test Abort}")
          self.station11Cmd["bg"] = "red"
          self.station11Text.set(s + "\nTest Aborted")
          return
        if self.GT1000.GT_Fail:
          print("{Test FAILED}")
          self.station11Cmd["bg"] = "red"
          self.station11Text.set(s + "\nTest FAILED")
          return
        if self.GT1000.GT_Pass:
          print("{Test PASSED}")
          self.station11Cmd["bg"] = "green"
          self.station11Text.set(s +"\n << PASSED >>")
          return
      self.station11Cmd["bg"] = "red"
      self.station11Cmd["activebackground"] = self.station11Cmd["bg"]
      self.station11Text.set(s + "\nAbnormal Completion")
  def station12Cmd__click(self):
    print("12")
    if self.testPart == "4569":
      self.station12Cmd["bg"] = "green"
      self.station12Cmd["activebackground"] = "green"
      return
    s = self.station12Text.get()
    self.GT1000.enableStations([14])
    self.station12Cmd["bg"] = "yellow"
    self.station12Cmd["activebackground"] = "yellow"
    self.station12Text.set(s + "\nIn Test")
    self.update()
    if self.GT1000.startTest() >= 1:
      while self.GT1000.GT_InTest:
        self.GT1000.read_inputs()
        if self.GT1000.GT_Abort:
          print("{Test Abort}")
          self.station12Cmd["bg"] = "red"
          self.station12Text.set(s + "\nTest Aborted")
          return
        if self.GT1000.GT_Fail:
          print("{Test FAILED}")
          self.station12Cmd["bg"] = "red"
          self.station12Text.set(s + "\nTest FAILED")
          return
        if self.GT1000.GT_Pass:
          print("{Test PASSED}")
          self.station12Cmd["bg"] = "green"
          self.station12Text.set(s +"\n << PASSED >>")
          return
      self.station12Cmd["bg"] = "red"
      self.station12Cmd["activebackground"] = self.station12Cmd["bg"]
      self.station12Text.set(s + "\nAbnormal Completion")
  def station13Cmd__click(self):
    print("13")
    if self.testPart == "4569":
      self.station13Cmd["bg"] = "green"
      self.station13Cmd["activebackground"] = "green"
      return
    s = self.station13Text.get()
    self.GT1000.enableStations([15])
    self.station13Cmd["bg"] = "yellow"
    self.station13Cmd["activebackground"] = "yellow"
    self.station13Text.set(s + "\nIn Test")
    self.update()
    if self.GT1000.startTest() >= 1:
      while self.GT1000.GT_InTest:
        self.GT1000.read_inputs()
        if self.GT1000.GT_Abort:
          print("{Test Abort}")
          self.station13Cmd["bg"] = "red"
          self.station13Text.set(s + "\nTest Aborted")
          return
        if self.GT1000.GT_Fail:
          print("{Test FAILED}")
          self.station13Cmd["bg"] = "red"
          self.station13Text.set(s + "\nTest FAILED")
          return
        if self.GT1000.GT_Pass:
          print("{Test PASSED}")
          self.station13Cmd["bg"] = "green"
          self.station13Text.set(s +"\n << PASSED >>")
          return
      self.station13Cmd["bg"] = "red"
      self.station13Cmd["activebackground"] = self.station13Cmd["bg"]
      self.station13Text.set(s + "\nAbnormal Completion")
  def station14Cmd__click(self):
    print("14")
    if self.testPart == "4569":
      self.station14Cmd["bg"] = "green"
      self.station14Cmd["activebackground"] = "green"
      return
    s = self.station14Text.get()
    self.GT1000.enableStations([16])
    self.station14Cmd["bg"] = "yellow"
    self.station14Cmd["activebackground"] = "yellow"
    self.station14Text.set(s + "\nIn Test")
    self.update()
    if self.GT1000.startTest() >= 1:
      while self.GT1000.GT_InTest:
        self.GT1000.read_inputs()
        if self.GT1000.GT_Abort:
          print("{Test Abort}")
          self.station14Cmd["bg"] = "red"
          self.station14Text.set(s + "\nTest Aborted")
          return
        if self.GT1000.GT_Fail:
          print("{Test FAILED}")
          self.station14Cmd["bg"] = "red"
          self.station14Text.set(s + "\nTest FAILED")
          return
        if self.GT1000.GT_Pass:
          print("{Test PASSED}")
          self.station14Cmd["bg"] = "green"
          self.station14Text.set(s +"\n << PASSED >>")
          return
      self.station14Cmd["bg"] = "red"
      self.station14Cmd["activebackground"] = self.station14Cmd["bg"]
      self.station14Text.set(s + "\nAbnormal Completion")
  def station15Cmd__click(self):
    print("15")
  def station16Cmd__click(self):
    print("<LOAD 4568>")
    self.testPart = "4568"
    self.resetButtonColours()
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
    self.resetButtonColours()
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
    if self.testingAll:
      return

    # Reset label colours
    self.station19Cmd__click()

    # Reset labels
    if self.testPart == "4569":
      self.station17Cmd__click()
    else:
      self.station16Cmd__click()
    self.abortSignal = False
    self.testingAll = True
    self.station01Cmd__click()
    self.GT1000.waitForIdle()
#    time.sleep(1)
#    self.GT1000.read_inputs()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.station02Cmd__click()
    self.GT1000.waitForIdle()
#    time.sleep(0.5)
#    self.GT1000.read_inputs()
    self.update()
    if self.abortSignal:
      self.testingAll = False
      self.abortSignal = False
      return
    self.station03Cmd__click()
    self.GT1000.waitForIdle()
#    time.sleep(0.5)
#    self.GT1000.read_inputs()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.station04Cmd__click()
    self.GT1000.waitForIdle()
#    time.sleep(0.5)
#    self.GT1000.read_inputs()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.station05Cmd__click()
    self.GT1000.waitForIdle()
#    time.sleep(0.5)
#    self.GT1000.read_inputs()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.station06Cmd__click()
    self.GT1000.waitForIdle()
#    time.sleep(0.5)
#    self.GT1000.read_inputs()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.station07Cmd__click()
    self.GT1000.waitForIdle()
#    time.sleep(0.5)
#    self.GT1000.read_inputs()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.station08Cmd__click()
    self.GT1000.waitForIdle()
#    time.sleep(0.5)
#    self.GT1000.read_inputs()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.station09Cmd__click()
    self.GT1000.waitForIdle()
#    time.sleep(0.5)
 #   self.GT1000.read_inputs()
    self.update()
    if self.abortSignal:
      self.testingAll = False
      self.abortSignal = False
      return
    self.station10Cmd__click()
    self.GT1000.waitForIdle()
#    time.sleep(0.5)
#    self.GT1000.read_inputs()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.station11Cmd__click()
    self.GT1000.waitForIdle()
#    time.sleep(0.5)
#    self.GT1000.read_inputs()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.station12Cmd__click()
    self.GT1000.waitForIdle()
#    time.sleep(0.5)
#    self.GT1000.read_inputs()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.station13Cmd__click()
#    time.sleep(0.5)
    self.GT1000.waitForIdle()
#    self.GT1000.read_inputs()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.station14Cmd__click()
#    self.GT1000.waitForIdle()
#    time.sleep(0.5)
    self.GT1000.read_inputs()
    self.update()
    self.checkForPass()
    self.testingAll = False

  def checkForPass(self):
    if (self.station01Cmd["bg"] == "green") and \
       (self.station02Cmd["bg"] == "green") and \
       (self.station03Cmd["bg"] == "green") and \
       (self.station04Cmd["bg"] == "green") and \
       (self.station05Cmd["bg"] == "green") and \
       (self.station06Cmd["bg"] == "green") and \
       (self.station07Cmd["bg"] == "green") and \
       (self.station08Cmd["bg"] == "green") and \
       (self.station09Cmd["bg"] == "green") and \
       (self.station10Cmd["bg"] == "green") and \
       (self.station11Cmd["bg"] == "green") and \
       (self.station12Cmd["bg"] == "green") and \
       (self.station13Cmd["bg"] == "green") and \
       (self.station14Cmd["bg"] == "green"):
      print("*** All Tests PASSED ***")
      self.GT1000.pulseRelease()

  def station19Cmd__click(self):
    print("<RESET>")
    self.abortSignal = True
    if self.testingAll:
      return
    self.resetButtonColours()
    if self.testPart == "4569":
      self.station17Cmd__click()
    else:
      self.station16Cmd__click()
    self.resetButtonColours()

  def station20Cmd__click(self):
    print("<NOTHING>")


  def resetButtonColours(self):
    print("resetButtonColours()")
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
