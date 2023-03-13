import tkinter as tk
from tkinter import *
from GT1000 import GT1000
import time
import os

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
    try:
      if (time.time() - self.lastAbortTick) > 5:
        if not self.GT1000.getLatchState():
          self.GT1000.latchReleaseEn()
      elif self.GT1000.getLatchState():
        self.GT1000.latchReleaseDis()
    except Exception as e:
      pass

    # Update part number based on selector switch
#    if self.testPart == "4568":
#      if self.GT1000.GT_PartSelect:
#        self.station17Cmd__click()
#    elif self.testPart == "4569":
#      if not self.GT1000.GT_PartSelect:
#        self.station16Cmd__click()
#    else:
#      self.station17Cmd__click()

    # Handle the start push
    if self.GT1000.GT_Start:
      self.station18Cmd__click()

    # Keep the updates coming
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


#    self.myScroll = Scrollbar(self)
 #   self.myScroll.grid(row=0,column=0)

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


    # H4569
    self.test200Text = StringVar()    # Start
    self.test20001Text = StringVar()  # Reset
    self.test20002Text = StringVar()  # H4568

    self.test201Text = StringVar()
    self.test20101Text = StringVar()
    self.test20102Text = StringVar()
    self.test20103Text = StringVar()
    self.test202Text = StringVar()
    self.test20201Text = StringVar()
    self.test20202Text = StringVar()
    self.test20203Text = StringVar()
    self.test20204Text = StringVar()
    self.test20205Text = StringVar()
    self.test20206Text = StringVar()
    self.test20207Text = StringVar()
    self.test20208Text = StringVar()
    self.test203Text = StringVar()
    self.test20301Text = StringVar()
    self.test204Text = StringVar()
    self.test20401Text = StringVar()
    self.test20402Text = StringVar()
    self.test20403Text = StringVar()
    self.test20404Text = StringVar()
    self.test20405Text = StringVar()
    self.test20406Text = StringVar()
    self.test205Text = StringVar()
    self.test20501Text = StringVar()
    self.test206Text = StringVar()
    self.test20601Text = StringVar()
    self.test207Text = StringVar()
    self.test20701Text = StringVar()
    self.test208Text = StringVar()
    self.test20801Text = StringVar()
    self.test209Text = StringVar()
    self.test20901Text = StringVar()
    self.test210Text = StringVar()
    self.test21001Text = StringVar()
    self.test211Text = StringVar()
    self.test21101Text = StringVar()
    self.test21102Text = StringVar()
    self.test21103Text = StringVar()
    self.test212Text = StringVar()
    self.test21201Text = StringVar()
    self.test21202Text = StringVar()
    self.test21203Text = StringVar()
    self.test213Text = StringVar()
    self.test21301Text = StringVar()
    self.test21302Text = StringVar()
    self.test21303Text = StringVar()
    self.test214Text = StringVar()
    self.test21401Text = StringVar()
    self.test21402Text = StringVar()
    self.test21403Text = StringVar()
    self.test215Text = StringVar()
    self.test21501Text = StringVar()
    self.test216Text = StringVar()
    self.test21601Text = StringVar()
    self.test217Text = StringVar()
    self.test21701Text = StringVar()
    self.test218Text = StringVar()
    self.test21801Text = StringVar()
    self.test219Text = StringVar()
    self.test21901Text = StringVar()
    self.test220Text = StringVar()
    self.test22001Text = StringVar()
    self.test22002Text = StringVar()
    self.test22003Text = StringVar()
    self.test22004Text = StringVar()
    self.test22005Text = StringVar()
    self.test221Text = StringVar()
    self.test22101Text = StringVar()
    self.test222Text = StringVar()
    self.test22201Text = StringVar()
    self.test223Text = StringVar()
    self.test22301Text = StringVar()
    self.test224Text = StringVar()
    self.test22401Text = StringVar()
    self.test22402Text = StringVar()
    self.test22403Text = StringVar()

    self.test200Text.set("Start")
    self.test20001Text.set("Reset")
    self.test20002Text.set("Test H4568")
    self.test201Text.set("ACM2.1")
    self.test20101Text.set("S201")
    self.test202Text.set("ACM2.2")
    self.test20201Text.set("GND 1")
    self.test20202Text.set("GND 2")
    self.test20203Text.set("GND 3")
    self.test20204Text.set("GND 4")
    self.test20205Text.set("GND 5")
    self.test20206Text.set("GND 6")
    self.test20207Text.set("GND 7")
    self.test20208Text.set("GND 8")
    self.test203Text.set("ACM2.3")
    self.test20301Text.set("S203")
    self.test204Text.set("ACM2.4")
    self.test20401Text.set("HELMET_FAN.A")
    self.test20402Text.set("PARTICULE.A")
    self.test20403Text.set("POST -")
    self.test20404Text.set("LED_CHASE_1.2")
    self.test20405Text.set("LED_CHASE_2.2")
    self.test20406Text.set("LED_CHASE_3.2")
    self.test205Text.set("ACM2.5")
    self.test20501Text.set("AFB2.H")
    self.test206Text.set("ACM2.10")
    self.test20601Text.set("S210")
    self.test207Text.set("ACM2.11")
    self.test20701Text.set("S211")
    self.test208Text.set("ACM2.12")
    self.test20801Text.set("S212")
    self.test209Text.set("ACM2.13")
    self.test20901Text.set("PARTICULE.C")
    self.test210Text.set("ACM2.14")
    self.test21001Text.set("HELMET_FAN.C")
    self.test211Text.set("ACM2.15")
    self.test21101Text.set("LED_CHASE_1.6")
    self.test21102Text.set("LED_CHASE_2.6")
    self.test21103Text.set("LED_CHASE_3.6")
    self.test212Text.set("ACM2.16")
    self.test21201Text.set("LED_CHASE_1.4")
    self.test21202Text.set("LED_CHASE_2.4")
    self.test21203Text.set("LED_CHASE_3.4")
    self.test213Text.set("ACM2.17")
    self.test21301Text.set("LED_CHASE_1.5")
    self.test21302Text.set("LED_CHASE_2.5")
    self.test21303Text.set("LED_CHASE_3.5")
    self.test214Text.set("ACM2.18")
    self.test21401Text.set("LED_CHASE_1.3")
    self.test21402Text.set("LED_CHASE_2.3")
    self.test21403Text.set("LED_CHASE_3.3")
    self.test215Text.set("ACM2.23")
    self.test21501Text.set("S223")
    self.test216Text.set("ACM2.25")
    self.test21601Text.set("S225")
    self.test217Text.set("ACM2.26")
    self.test21701Text.set("S226")
    self.test218Text.set("ACM2.27")
    self.test21801Text.set("S227")
    self.test219Text.set("ACM2.28")
    self.test21901Text.set("S228")
    self.test220Text.set("AFB2.A")
    self.test22001Text.set("LED_CHASE_1.1")
    self.test22002Text.set("LED_CHASE_2.1")
    self.test22003Text.set("LED_CHASE_3.1")
    self.test22004Text.set(" ")
    self.test22005Text.set(" ")
    self.test221Text.set("AFB2.D")
    self.test22101Text.set("HELMET_FAN.B")
    self.test222Text.set("AFB2.E")
    self.test22201Text.set("PARTICULE.B")
    self.test223Text.set("POST +")
    self.test22301Text.set("AFB2.G")
    self.test224Text.set("POST ACC +")
    self.test22401Text.set("AFB2.B")
    self.test22402Text.set("AFB2.D")
    self.test22403Text.set("AFB2.E")

    # H4568
    self.test00Text = StringVar()
    self.test0001Text = StringVar()
    self.test0002Text = StringVar()
    self.test0003Text = StringVar()

    self.test01Text = StringVar()
    self.test0101Text = StringVar()
    self.test02Text = StringVar()
    self.test0201Text = StringVar()
    self.test0202Text = StringVar()
    self.test0203Text = StringVar()
    self.test0204Text = StringVar()
    self.test0205Text = StringVar()
    self.test0206Text = StringVar()
    self.test0207Text = StringVar()
    self.test0208Text = StringVar()
    self.test0209Text = StringVar()
    self.test03Text = StringVar()
    self.test0301Text = StringVar()
    self.test04Text = StringVar()
    self.test0401Text = StringVar()
    self.test0402Text = StringVar()
    self.test0403Text = StringVar()
    self.test0404Text = StringVar()
    self.test0405Text = StringVar()
    self.test0406Text = StringVar()
    self.test05Text = StringVar()
    self.test0501Text = StringVar()
    self.test06Text = StringVar()
    self.test0601Text = StringVar()
    self.test0602Text = StringVar()
    self.test07Text = StringVar()
    self.test0701Text = StringVar()
    self.test08Text = StringVar()
    self.test0801Text = StringVar()
    self.test0802Text = StringVar()
    self.test09Text = StringVar()
    self.test0901Text = StringVar()
    self.test10Text = StringVar()
    self.test1001Text = StringVar()
    self.test11Text = StringVar()
    self.test1101Text = StringVar()
    self.test1102Text = StringVar()
    self.test1103Text = StringVar()
    self.test12Text = StringVar()
    self.test1201Text = StringVar()
    self.test13Text = StringVar()
    self.test1301Text = StringVar()
    self.test14Text = StringVar()
    self.test1401Text = StringVar()
    self.test1402Text = StringVar()
    self.test1403Text = StringVar()
    self.test15Text = StringVar()
    self.test1501Text = StringVar()
    self.test1502Text = StringVar()
    self.test1503Text = StringVar()
    self.test16Text = StringVar()
    self.test1601Text = StringVar()
    self.test17Text = StringVar()
    self.test1701Text = StringVar()
    self.test18Text = StringVar()
    self.test1801Text = StringVar()
    self.test19Text = StringVar()
    self.test1901Text = StringVar()
    self.test20Text = StringVar()
    self.test2001Text = StringVar()
    self.test21Text = StringVar()
    self.test2101Text = StringVar()
    self.test22Text = StringVar()
    self.test2201Text = StringVar()
    self.test23Text = StringVar()
    self.test2301Text = StringVar()
    self.test24Text = StringVar()
    self.test2401Text = StringVar()
    self.test25Text = StringVar()
    self.test2501Text = StringVar()
    self.test2502Text = StringVar()
    self.test26Text = StringVar()
    self.test2601Text = StringVar()
    self.test27Text = StringVar()
    self.test2701Text = StringVar()
    self.test2702Text = StringVar()
    self.test2703Text = StringVar()
    self.test28Text = StringVar()
    self.test2801Text = StringVar()
    self.test29Text = StringVar()
    self.test2901Text = StringVar()
    self.test2902Text = StringVar()
    self.test30Text = StringVar()
    self.test3001Text = StringVar()
    self.test31Text = StringVar()
    self.test3101Text = StringVar()
    self.test3102Text = StringVar()
    self.test32Text = StringVar()
    self.test3201Text = StringVar()
    self.test3202Text = StringVar()
    self.test3203Text = StringVar()
    self.test33Text = StringVar()
    self.test3301Text = StringVar()
    self.test3302Text = StringVar()
    self.test34Text = StringVar()
    self.test3401Text = StringVar()
    self.test35Text = StringVar()
    self.test3501Text = StringVar()
    self.test36Text = StringVar()
    self.test3601Text = StringVar()
    self.test3602Text = StringVar()
    self.test3603Text = StringVar()
    self.test3604Text = StringVar()
    self.test3605Text = StringVar()
    self.test37Text = StringVar()
    self.test3701Text = StringVar()
    self.test3702Text = StringVar()
    self.test38Text = StringVar()
    self.test39Text = StringVar()
    self.test40Text = StringVar()
    self.test41Text = StringVar()
    self.test42Text = StringVar()


    self.test00Text.set("Start")
    self.test0001Text.set("Reset")
    self.test0002Text.set("Test H4569")
    self.test0003Text.set("Shut Down")
    self.test01Text.set("ACM1.1")
    self.test0101Text.set("AFB1.E3")
    self.test02Text.set("ACM1.2")
    self.test0201Text.set("LED_L.A")
    self.test0202Text.set("LED_R.A")
    self.test0203Text.set("POST -")
    self.test0204Text.set("WIPER.1")
    self.test0205Text.set("SW_1.7")
    self.test0206Text.set("LED_HOOD.A")
    self.test0207Text.set("LED_BUMPER.2")
    self.test0208Text.set("RED_ROOF.1")
    self.test0209Text.set("LED_ROOF.2")
    self.test03Text.set("ACM1.3")
    self.test0301Text.set("PWR_FLIP.1")
    self.test04Text.set("ACM1.4")
    self.test0401Text.set("AFB1.C3")
    self.test0402Text.set("GND 1")
    self.test0403Text.set("GND 2")
    self.test0404Text.set("WASHER.1")
    self.test0405Text.set("AFB1.C6")
    self.test0406Text.set("AFB1.A6")
    self.test05Text.set("ACM1.5")
    self.test0501Text.set("PWR_FLIP.1")
    self.test06Text.set("ACM1.6")
    self.test0601Text.set("LED_ROOF.3")
    self.test0602Text.set("AFB1.D4")
    self.test07Text.set("ACM1.7")
    self.test0701Text.set("LED_ROOF.6")
    self.test08Text.set("ACM1.8")
    self.test0801Text.set("LED_BUMPER.3")
    self.test0802Text.set("AFB1.B4")
    self.test09Text.set("ACM1.9")
    self.test0901Text.set("LED_BUMPER.6")
    self.test10Text.set("ACM1.10")
    self.test1001Text.set("LED_HOOD.B")
    self.test11Text.set("ACM1.11")
    self.test1101Text.set("DLC1.6")
    self.test1102Text.set("DLC2.6")
    self.test1103Text.set("KEY_PAD.6")
    self.test12Text.set("ACM1.12")
    self.test1201Text.set("SNS.1")
    self.test13Text.set("ACM1.13")
    self.test1301Text.set("SNS.2")
    self.test14Text.set("ACM1.14")
    self.test1401Text.set("DLC1.1")
    self.test1402Text.set("DLC2.1")
    self.test1403Text.set("KEY_PAD.2")
    self.test15Text.set("ACM1.15")
    self.test1501Text.set("DLC1.2")
    self.test1502Text.set("DLC2.2")
    self.test1503Text.set("KEY_PAD.5")
    self.test16Text.set("ACM1.18")
    self.test1601Text.set("LED_HOOD.D")
    self.test17Text.set("ACM1.19")
    self.test1701Text.set("SW_1.3")
    self.test18Text.set("ACM1.20")
    self.test1801Text.set("SW_1.1")
    self.test19Text.set("ACM1.21")
    self.test1901Text.set("LED_L.C")
    self.test20Text.set("ACM1.22")
    self.test2001Text.set("LED_R.C")
    self.test21Text.set("ACM1.25")
    self.test2101Text.set("AFB1.D1")
    self.test22Text.set("ACM1.26")
    self.test2201Text.set("WASHER.2")
    self.test23Text.set("ACM1.27")
    self.test2301Text.set("S127")
    self.test24Text.set("ACM1.28")
    self.test2401Text.set("S128")
    self.test25Text.set("AFB1.B5")
    self.test2501Text.set("AFB1.A4")
    self.test2502Text.set("AFB1.E5")
    self.test26Text.set("AFB1.B6")
    self.test2601Text.set("LED_BUMPER.4")
    self.test27Text.set("AFB1.C1")
    self.test2701Text.set("AFB1.F1")
    self.test2702Text.set("WIPER.4")
    self.test28Text.set("AFB1.C2")
    self.test2801Text.set("WIPER.2")
    self.test29Text.set("AFB1.C4")
    self.test2901Text.set("AFB1.D5")
    self.test2902Text.set("AFB1.F5")
    self.test30Text.set("AFB1.D3")
    self.test3001Text.set("WIPER.3")
    self.test31Text.set("AFB1.D6")
    self.test3101Text.set("LED_ROOF.4")
    self.test3102Text.set("LED_ROOF.5")
    self.test32Text.set("AFB1.E1")
    self.test3201Text.set("LED_L.B")
    self.test3202Text.set("LED_R.B")
    self.test3203Text.set("LED_HOOD.C")
    self.test33Text.set("DLC1.3")
    self.test3301Text.set("DLC2.3")
    self.test3302Text.set("KEY_PAD.1")
    self.test34Text.set("DLC1.4")
    self.test3401Text.set("DLC2.4")
    self.test35Text.set("DLC1.5")
    self.test3501Text.set("DLC2.5")
    self.test36Text.set("POST +")
    self.test3601Text.set("AFB1.E4")
    self.test3602Text.set("AFB1.F2")
    self.test3603Text.set("AFB1.E2")
    self.test3604Text.set("AFB1.E6")
    self.test3605Text.set("AFB1.F6")
    self.test37Text.set("POST ACC +")
    self.test3701Text.set("SW_1.2")
    self.test3702Text.set("SW_1.8")
    self.test38Text.set("ACM1.1")
    self.test39Text.set("ACM1.1")
    self.test40Text.set("ACM1.1")
    self.test41Text.set("ACM1.1")
    self.test42Text.set("ACM1.1")





    # Some parameters
    gridWidth = 11
    gridHeight = 3
    rowIndex = 0
    fontHeight = 8


    self.canvasScroll = Scrollbar(self, orient=VERTICAL, width=50,jump=1)
    self.canvasScroll.pack(fill=Y, side=RIGHT, expand=FALSE)
    self.mainCanvas = Canvas(self,bd=0,highlightthickness=0,yscrollcommand=self.canvasScroll.set,yscrollincrement='400')
    self.mainCanvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
    self.main2Canvas = Canvas(self,bd=0,highlightthickness=0,yscrollcommand=self.canvasScroll.set,yscrollincrement='400')
#    self.main2Canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
    self.canvasScroll.config(command=self.mainCanvas.yview)
    self.mainCanvas.xview_moveto(0)
    self.mainCanvas.yview_moveto(0)
    self.main2Canvas.xview_moveto(0)
    self.main2Canvas.yview_moveto(0)
    self.mainFrame = Frame(self)
    self.main2Frame = Frame(self)

    self.main2Canvas.create_window(0,0,window=self.main2Frame,anchor=NW)

    # Start/Stop buttons // Add button for H4569 swap
    self.test200Cmd = Button(self.main2Frame, textvariable=self.test200Text,command=self.test200Cmd__click,height=gridHeight*3,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test200Cmd.grid(row=0,column=7,sticky='w',rowspan=2)
    self.test20001Cmd = Button(self.main2Frame, textvariable=self.test20001Text,command=self.test20001Cmd__click,height=gridHeight*3,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test20001Cmd.grid(row=2,column=7,sticky='w',rowspan=2)
    self.test20002Cmd = Button(self.main2Frame, textvariable=self.test20002Text,command=self.test20002Cmd__click,height=gridHeight*3,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test20002Cmd.grid(row=4,column=7,sticky='w',rowspan=2)

    # Test 1
    self.test201Cmd = Button(self.main2Frame, textvariable=self.test201Text,command=self.test201Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test201Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test20101Cmd = Button(self.main2Frame, textvariable=self.test20101Text,command=self.test20101Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test20101Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 2
    rowIndex += 1
    self.test202Cmd = Button(self.main2Frame, textvariable=self.test202Text,command=self.test202Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test202Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test20201Cmd = Button(self.main2Frame, textvariable=self.test20201Text,command=self.test20201Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test20201Cmd.grid(row=rowIndex,column=1,sticky='w')
    self.test20202Cmd = Button(self.main2Frame, textvariable=self.test20202Text,command=self.test20202Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test20202Cmd.grid(row=rowIndex,column=2,sticky='w')
    self.test20203Cmd = Button(self.main2Frame, textvariable=self.test20203Text,command=self.test20203Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test20203Cmd.grid(row=rowIndex,column=3,sticky='w')
    self.test20204Cmd = Button(self.main2Frame, textvariable=self.test20204Text,command=self.test20204Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test20204Cmd.grid(row=rowIndex,column=4,sticky='w')
    self.test20205Cmd = Button(self.main2Frame, textvariable=self.test20205Text,command=self.test20205Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test20205Cmd.grid(row=rowIndex,column=5,sticky='w')
    rowIndex += 1
    self.test20206Cmd = Button(self.main2Frame, textvariable=self.test20206Text,command=self.test20206Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test20206Cmd.grid(row=rowIndex,column=1,sticky='w')
    self.test20207Cmd = Button(self.main2Frame, textvariable=self.test20207Text,command=self.test20207Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test20207Cmd.grid(row=rowIndex,column=2,sticky='w')
    self.test20208Cmd = Button(self.main2Frame, textvariable=self.test20208Text,command=self.test20208Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test20208Cmd.grid(row=rowIndex,column=3,sticky='w')

    # Test 3
    rowIndex += 1
    self.test203Cmd = Button(self.main2Frame, textvariable=self.test203Text,command=self.test203Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test203Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test20301Cmd = Button(self.main2Frame, textvariable=self.test20301Text,command=self.test20301Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test20301Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 4
    rowIndex += 1
    self.test204Cmd = Button(self.main2Frame, textvariable=self.test204Text,command=self.test204Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test204Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test20401Cmd = Button(self.main2Frame, textvariable=self.test20401Text,command=self.test20401Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test20401Cmd.grid(row=rowIndex,column=1,sticky='w')
    self.test20402Cmd = Button(self.main2Frame, textvariable=self.test20402Text,command=self.test20402Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test20402Cmd.grid(row=rowIndex,column=2,sticky='w')
    self.test20403Cmd = Button(self.main2Frame, textvariable=self.test20403Text,command=self.test20403Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test20403Cmd.grid(row=rowIndex,column=3,sticky='w')
    self.test20404Cmd = Button(self.main2Frame, textvariable=self.test20404Text,command=self.test20404Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test20404Cmd.grid(row=rowIndex,column=4,sticky='w')
    self.test20405Cmd = Button(self.main2Frame, textvariable=self.test20405Text,command=self.test20405Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test20405Cmd.grid(row=rowIndex,column=5,sticky='w')
    rowIndex += 1
    self.test20406Cmd = Button(self.main2Frame, textvariable=self.test20406Text,command=self.test20406Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test20406Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 5
    rowIndex += 1
    self.test205Cmd = Button(self.main2Frame, textvariable=self.test205Text,command=self.test205Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test205Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test20501Cmd = Button(self.main2Frame, textvariable=self.test20501Text,command=self.test20501Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test20501Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 6
    rowIndex += 1
    self.test206Cmd = Button(self.main2Frame, textvariable=self.test206Text,command=self.test206Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test206Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test20601Cmd = Button(self.main2Frame, textvariable=self.test20601Text,command=self.test20601Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test20601Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 7
    rowIndex += 1
    self.test207Cmd = Button(self.main2Frame, textvariable=self.test207Text,command=self.test207Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test207Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test20701Cmd = Button(self.main2Frame, textvariable=self.test20701Text,command=self.test20701Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test20701Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 8
    rowIndex += 1
    self.test208Cmd = Button(self.main2Frame, textvariable=self.test208Text,command=self.test208Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test208Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test20801Cmd = Button(self.main2Frame, textvariable=self.test20801Text,command=self.test20801Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test20801Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 9
    rowIndex += 1
    self.test209Cmd = Button(self.main2Frame, textvariable=self.test209Text,command=self.test209Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test209Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test20901Cmd = Button(self.main2Frame, textvariable=self.test20901Text,command=self.test20901Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test20901Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 10
    rowIndex += 1
    self.test210Cmd = Button(self.main2Frame, textvariable=self.test210Text,command=self.test210Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test210Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test21001Cmd = Button(self.main2Frame, textvariable=self.test21001Text,command=self.test21001Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test21001Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 11
    rowIndex += 1
    self.test211Cmd = Button(self.main2Frame, textvariable=self.test211Text,command=self.test211Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test211Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test21101Cmd = Button(self.main2Frame, textvariable=self.test21101Text,command=self.test21101Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test21101Cmd.grid(row=rowIndex,column=1,sticky='w')
    self.test21102Cmd = Button(self.main2Frame, textvariable=self.test21102Text,command=self.test21102Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test21102Cmd.grid(row=rowIndex,column=2,sticky='w')
    self.test21103Cmd = Button(self.main2Frame, textvariable=self.test21103Text,command=self.test21103Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test21103Cmd.grid(row=rowIndex,column=3,sticky='w')

    # Test 12
    rowIndex += 1
    self.test212Cmd = Button(self.main2Frame, textvariable=self.test212Text,command=self.test212Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test212Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test21201Cmd = Button(self.main2Frame, textvariable=self.test21201Text,command=self.test21201Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test21201Cmd.grid(row=rowIndex,column=1,sticky='w')
    self.test21202Cmd = Button(self.main2Frame, textvariable=self.test21202Text,command=self.test21202Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test21202Cmd.grid(row=rowIndex,column=2,sticky='w')
    self.test21203Cmd = Button(self.main2Frame, textvariable=self.test21203Text,command=self.test21203Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test21203Cmd.grid(row=rowIndex,column=3,sticky='w')

    # Test 13
    rowIndex += 1
    self.test213Cmd = Button(self.main2Frame, textvariable=self.test213Text,command=self.test213Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test213Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test21301Cmd = Button(self.main2Frame, textvariable=self.test21301Text,command=self.test21301Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test21301Cmd.grid(row=rowIndex,column=1,sticky='w')
    self.test21302Cmd = Button(self.main2Frame, textvariable=self.test21302Text,command=self.test21302Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test21302Cmd.grid(row=rowIndex,column=2,sticky='w')
    self.test21303Cmd = Button(self.main2Frame, textvariable=self.test21303Text,command=self.test21303Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test21303Cmd.grid(row=rowIndex,column=3,sticky='w')

    # Test 14
    rowIndex += 1
    self.test214Cmd = Button(self.main2Frame, textvariable=self.test214Text,command=self.test214Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test214Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test21401Cmd = Button(self.main2Frame, textvariable=self.test21401Text,command=self.test21401Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test21401Cmd.grid(row=rowIndex,column=1,sticky='w')
    self.test21402Cmd = Button(self.main2Frame, textvariable=self.test21402Text,command=self.test21402Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test21402Cmd.grid(row=rowIndex,column=2,sticky='w')
    self.test21403Cmd = Button(self.main2Frame, textvariable=self.test21403Text,command=self.test21403Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test21403Cmd.grid(row=rowIndex,column=3,sticky='w')

    # Test 15
    rowIndex += 1
    self.test215Cmd = Button(self.main2Frame, textvariable=self.test215Text,command=self.test215Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test215Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test21501Cmd = Button(self.main2Frame, textvariable=self.test21501Text,command=self.test21501Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test21501Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 16
    rowIndex += 1
    self.test216Cmd = Button(self.main2Frame, textvariable=self.test216Text,command=self.test216Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test216Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test21601Cmd = Button(self.main2Frame, textvariable=self.test21601Text,command=self.test21601Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test21601Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 17
    rowIndex += 1
    self.test217Cmd = Button(self.main2Frame, textvariable=self.test217Text,command=self.test217Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test217Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test21701Cmd = Button(self.main2Frame, textvariable=self.test21701Text,command=self.test21701Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test21701Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 18
    rowIndex += 1
    self.test218Cmd = Button(self.main2Frame, textvariable=self.test218Text,command=self.test218Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test218Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test21801Cmd = Button(self.main2Frame, textvariable=self.test21801Text,command=self.test21801Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test21801Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 19
    rowIndex += 1
    self.test219Cmd = Button(self.main2Frame, textvariable=self.test219Text,command=self.test219Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test219Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test21901Cmd = Button(self.main2Frame, textvariable=self.test21901Text,command=self.test21901Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test21901Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 20
    rowIndex += 1
    self.test220Cmd = Button(self.main2Frame, textvariable=self.test220Text,command=self.test220Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test220Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test22001Cmd = Button(self.main2Frame, textvariable=self.test22001Text,command=self.test22001Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test22001Cmd.grid(row=rowIndex,column=1,sticky='w')
    self.test22002Cmd = Button(self.main2Frame, textvariable=self.test22002Text,command=self.test22002Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test22002Cmd.grid(row=rowIndex,column=2,sticky='w')
    self.test22003Cmd = Button(self.main2Frame, textvariable=self.test22003Text,command=self.test22003Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test22003Cmd.grid(row=rowIndex,column=3,sticky='w')
#    self.test22004Cmd = Button(self.main2Frame, textvariable=self.test22004Text,command=self.test22004Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
#    self.test22004Cmd.grid(row=rowIndex,column=4,sticky='w')
#    self.test22005Cmd = Button(self.main2Frame, textvariable=self.test22005Text,command=self.test22005Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
#    self.test22005Cmd.grid(row=rowIndex,column=5,sticky='w')

    # Test 21
    rowIndex += 1
    self.test221Cmd = Button(self.main2Frame, textvariable=self.test221Text,command=self.test221Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test221Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test22101Cmd = Button(self.main2Frame, textvariable=self.test22101Text,command=self.test22101Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test22101Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 22
    rowIndex += 1
    self.test222Cmd = Button(self.main2Frame, textvariable=self.test222Text,command=self.test222Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test222Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test22201Cmd = Button(self.main2Frame, textvariable=self.test22201Text,command=self.test22201Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test22201Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 23
    rowIndex += 1
    self.test223Cmd = Button(self.main2Frame, textvariable=self.test223Text,command=self.test223Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test223Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test22301Cmd = Button(self.main2Frame, textvariable=self.test22301Text,command=self.test22301Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test22301Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 24
    rowIndex += 1
    self.test224Cmd = Button(self.main2Frame, textvariable=self.test224Text,command=self.test224Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test224Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test22401Cmd = Button(self.main2Frame, textvariable=self.test22401Text,command=self.test22401Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test22401Cmd.grid(row=rowIndex,column=1,sticky='w')
    self.test22402Cmd = Button(self.main2Frame, textvariable=self.test22402Text,command=self.test22402Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test22402Cmd.grid(row=rowIndex,column=2,sticky='w')
    self.test22403Cmd = Button(self.main2Frame, textvariable=self.test22403Text,command=self.test22403Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test22403Cmd.grid(row=rowIndex,column=3,sticky='w')



    ##  &&&&&&&&&&&&&&&&&&&&&&&&&
    ## <<< Start of Main Frame >>>
    ##  &&&&&&&&&&&&&&&&&&&&&&&&&

    rowIndex = 0
    self.mainCanvas.create_window(0,0,window=self.mainFrame,anchor=NW)

    # Start/Stop buttons // Add button for H4569 swap
    self.test00Cmd = Button(self.mainFrame, textvariable=self.test00Text,command=self.test00Cmd__click,height=gridHeight*3,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test00Cmd.grid(row=0,column=7,sticky='w',rowspan=2)
    self.test0001Cmd = Button(self.mainFrame, textvariable=self.test0001Text,command=self.test0001Cmd__click,height=gridHeight*3,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test0001Cmd.grid(row=2,column=7,sticky='w',rowspan=2)
    self.test0002Cmd = Button(self.mainFrame, textvariable=self.test0002Text,command=self.test0002Cmd__click,height=gridHeight*3,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test0002Cmd.grid(row=4,column=7,sticky='w',rowspan=2)
    self.test0003Cmd = Button(self.mainFrame, textvariable=self.test0003Text,command=self.test0003Cmd__click,height=gridHeight*3,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test0003Cmd.grid(row=12,column=7,sticky='w',rowspan=2)

    # Test 1
    self.test01Cmd = Button(self.mainFrame, textvariable=self.test01Text,command=self.test01Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test01Cmd.grid(row=0,column=0,sticky='w')
    self.test0101Cmd = Button(self.mainFrame, textvariable=self.test0101Text,command=self.test0101Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test0101Cmd.grid(row=0,column=1,sticky='w')

    # Test 2
    rowIndex += 1
    self.test02Cmd = Button(self.mainFrame, textvariable=self.test02Text,command=self.test02Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test02Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test0201Cmd = Button(self.mainFrame, textvariable=self.test0201Text,command=self.test0201Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test0201Cmd.grid(row=rowIndex,column=1,sticky='w')
    self.test0202Cmd = Button(self.mainFrame, textvariable=self.test0202Text,command=self.test0202Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test0202Cmd.grid(row=rowIndex,column=2,sticky='w')
    self.test0203Cmd = Button(self.mainFrame, textvariable=self.test0203Text,command=self.test0203Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test0203Cmd.grid(row=rowIndex,column=3,sticky='w')
    self.test0204Cmd = Button(self.mainFrame, textvariable=self.test0204Text,command=self.test0204Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test0204Cmd.grid(row=rowIndex,column=4,sticky='w')
    self.test0205Cmd = Button(self.mainFrame, textvariable=self.test0205Text,command=self.test0205Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test0205Cmd.grid(row=rowIndex,column=5,sticky='w')
    rowIndex += 1
    self.test0206Cmd = Button(self.mainFrame, textvariable=self.test0206Text,command=self.test0206Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test0206Cmd.grid(row=rowIndex,column=1,sticky='w')
    self.test0207Cmd = Button(self.mainFrame, textvariable=self.test0207Text,command=self.test0207Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test0207Cmd.grid(row=rowIndex,column=2,sticky='w')
    self.test0208Cmd = Button(self.mainFrame, textvariable=self.test0208Text,command=self.test0208Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test0208Cmd.grid(row=rowIndex,column=3,sticky='w')
    self.test0209Cmd = Button(self.mainFrame, textvariable=self.test0209Text,command=self.test0209Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test0209Cmd.grid(row=rowIndex,column=4,sticky='w')

    # Test 3
    rowIndex += 1
    self.test03Cmd = Button(self.mainFrame, textvariable=self.test03Text,command=self.test03Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test03Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test0301Cmd = Button(self.mainFrame, textvariable=self.test0301Text,command=self.test0301Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test0301Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 4
    rowIndex += 1
    self.test04Cmd = Button(self.mainFrame, textvariable=self.test04Text,command=self.test04Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test04Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test0401Cmd = Button(self.mainFrame, textvariable=self.test0401Text,command=self.test0401Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test0401Cmd.grid(row=rowIndex,column=1,sticky='w')
    self.test0402Cmd = Button(self.mainFrame, textvariable=self.test0402Text,command=self.test0402Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test0402Cmd.grid(row=rowIndex,column=2,sticky='w')
    self.test0403Cmd = Button(self.mainFrame, textvariable=self.test0403Text,command=self.test0403Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test0403Cmd.grid(row=rowIndex,column=3,sticky='w')
    self.test0404Cmd = Button(self.mainFrame, textvariable=self.test0404Text,command=self.test0404Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test0404Cmd.grid(row=rowIndex,column=4,sticky='w')
    self.test0405Cmd = Button(self.mainFrame, textvariable=self.test0405Text,command=self.test0405Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test0405Cmd.grid(row=rowIndex,column=5,sticky='w')
    rowIndex += 1
    self.test0406Cmd = Button(self.mainFrame, textvariable=self.test0406Text,command=self.test0406Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test0406Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 5
    rowIndex += 1
    self.test05Cmd = Button(self.mainFrame, textvariable=self.test05Text,command=self.test05Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test05Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test0501Cmd = Button(self.mainFrame, textvariable=self.test0501Text,command=self.test0501Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test0501Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 6
    rowIndex += 1
    self.test06Cmd = Button(self.mainFrame, textvariable=self.test06Text,command=self.test06Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test06Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test0601Cmd = Button(self.mainFrame, textvariable=self.test0601Text,command=self.test0601Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test0601Cmd.grid(row=rowIndex,column=1,sticky='w')
    self.test0602Cmd = Button(self.mainFrame, textvariable=self.test0602Text,command=self.test0602Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test0602Cmd.grid(row=rowIndex,column=2,sticky='w')

    # Test 7
    rowIndex += 1
    self.test07Cmd = Button(self.mainFrame, textvariable=self.test07Text,command=self.test07Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test07Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test0701Cmd = Button(self.mainFrame, textvariable=self.test0701Text,command=self.test0701Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test0701Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 8
    rowIndex += 1
    self.test08Cmd = Button(self.mainFrame, textvariable=self.test08Text,command=self.test08Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test08Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test0801Cmd = Button(self.mainFrame, textvariable=self.test0801Text,command=self.test0801Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test0801Cmd.grid(row=rowIndex,column=1,sticky='w')
    self.test0802Cmd = Button(self.mainFrame, textvariable=self.test0802Text,command=self.test0802Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test0802Cmd.grid(row=rowIndex,column=2,sticky='w')

    # Test 9
    rowIndex += 1
    self.test09Cmd = Button(self.mainFrame, textvariable=self.test09Text,command=self.test09Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test09Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test0901Cmd = Button(self.mainFrame, textvariable=self.test0901Text,command=self.test0901Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test0901Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 10
    rowIndex += 1
    self.test10Cmd = Button(self.mainFrame, textvariable=self.test10Text,command=self.test10Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test10Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test1001Cmd = Button(self.mainFrame, textvariable=self.test1001Text,command=self.test1001Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test1001Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 11
    rowIndex += 1
    self.test11Cmd = Button(self.mainFrame, textvariable=self.test11Text,command=self.test11Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test11Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test1101Cmd = Button(self.mainFrame, textvariable=self.test1101Text,command=self.test1101Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test1101Cmd.grid(row=rowIndex,column=1,sticky='w')
    self.test1102Cmd = Button(self.mainFrame, textvariable=self.test1102Text,command=self.test1102Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test1102Cmd.grid(row=rowIndex,column=2,sticky='w')
    self.test1103Cmd = Button(self.mainFrame, textvariable=self.test1103Text,command=self.test1103Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test1103Cmd.grid(row=rowIndex,column=3,sticky='w')

    # Test 12
    rowIndex += 1
    self.test12Cmd = Button(self.mainFrame, textvariable=self.test12Text,command=self.test12Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test12Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test1201Cmd = Button(self.mainFrame, textvariable=self.test1201Text,command=self.test1201Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test1201Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 13
    rowIndex += 1
    self.test13Cmd = Button(self.mainFrame, textvariable=self.test13Text,command=self.test13Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test13Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test1301Cmd = Button(self.mainFrame, textvariable=self.test1301Text,command=self.test1301Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test1301Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 14
    rowIndex += 1
    self.test14Cmd = Button(self.mainFrame, textvariable=self.test14Text,command=self.test14Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test14Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test1401Cmd = Button(self.mainFrame, textvariable=self.test1401Text,command=self.test1401Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test1401Cmd.grid(row=rowIndex,column=1,sticky='w')
    self.test1402Cmd = Button(self.mainFrame, textvariable=self.test1402Text,command=self.test1402Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test1402Cmd.grid(row=rowIndex,column=2,sticky='w')
    self.test1403Cmd = Button(self.mainFrame, textvariable=self.test1403Text,command=self.test1403Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test1403Cmd.grid(row=rowIndex,column=3,sticky='w')

    # Test 15
    rowIndex += 1
    self.test15Cmd = Button(self.mainFrame, textvariable=self.test15Text,command=self.test15Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test15Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test1501Cmd = Button(self.mainFrame, textvariable=self.test1501Text,command=self.test1501Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test1501Cmd.grid(row=rowIndex,column=1,sticky='w')
    self.test1502Cmd = Button(self.mainFrame, textvariable=self.test1502Text,command=self.test1502Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test1502Cmd.grid(row=rowIndex,column=2,sticky='w')
    self.test1503Cmd = Button(self.mainFrame, textvariable=self.test1503Text,command=self.test1503Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test1503Cmd.grid(row=rowIndex,column=3,sticky='w')

    # Test 16
    rowIndex += 1
    self.test16Cmd = Button(self.mainFrame, textvariable=self.test16Text,command=self.test16Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test16Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test1601Cmd = Button(self.mainFrame, textvariable=self.test1601Text,command=self.test1601Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test1601Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 17
    rowIndex += 1
    self.test17Cmd = Button(self.mainFrame, textvariable=self.test17Text,command=self.test17Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test17Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test1701Cmd = Button(self.mainFrame, textvariable=self.test1701Text,command=self.test1701Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test1701Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 18
    rowIndex += 1
    self.test18Cmd = Button(self.mainFrame, textvariable=self.test18Text,command=self.test18Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test18Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test1801Cmd = Button(self.mainFrame, textvariable=self.test1801Text,command=self.test1801Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test1801Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 19
    rowIndex += 1
    self.test19Cmd = Button(self.mainFrame, textvariable=self.test19Text,command=self.test19Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test19Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test1901Cmd = Button(self.mainFrame, textvariable=self.test1901Text,command=self.test1901Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test1901Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 20
    rowIndex += 1
    self.test20Cmd = Button(self.mainFrame, textvariable=self.test20Text,command=self.test20Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test20Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test2001Cmd = Button(self.mainFrame, textvariable=self.test2001Text,command=self.test2001Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test2001Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 21
    rowIndex += 1
    self.test21Cmd = Button(self.mainFrame, textvariable=self.test21Text,command=self.test21Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test21Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test2101Cmd = Button(self.mainFrame, textvariable=self.test2101Text,command=self.test2101Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test2101Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 22
    rowIndex += 1
    self.test22Cmd = Button(self.mainFrame, textvariable=self.test22Text,command=self.test22Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test22Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test2201Cmd = Button(self.mainFrame, textvariable=self.test2201Text,command=self.test2201Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test2201Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 23
    rowIndex += 1
    self.test23Cmd = Button(self.mainFrame, textvariable=self.test23Text,command=self.test23Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test23Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test2301Cmd = Button(self.mainFrame, textvariable=self.test2301Text,command=self.test2301Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test2301Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 24
    rowIndex += 1
    self.test24Cmd = Button(self.mainFrame, textvariable=self.test24Text,command=self.test24Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test24Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test2401Cmd = Button(self.mainFrame, textvariable=self.test2401Text,command=self.test2401Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test2401Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 25
    rowIndex += 1
    self.test25Cmd = Button(self.mainFrame, textvariable=self.test25Text,command=self.test25Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test25Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test2501Cmd = Button(self.mainFrame, textvariable=self.test2501Text,command=self.test2501Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test2501Cmd.grid(row=rowIndex,column=1,sticky='w')
    self.test2502Cmd = Button(self.mainFrame, textvariable=self.test2502Text,command=self.test2502Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test2502Cmd.grid(row=rowIndex,column=2,sticky='w')

    # Test 26
    rowIndex += 1
    self.test26Cmd = Button(self.mainFrame, textvariable=self.test26Text,command=self.test26Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test26Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test2601Cmd = Button(self.mainFrame, textvariable=self.test2601Text,command=self.test2601Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test2601Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 27
    rowIndex += 1
    self.test27Cmd = Button(self.mainFrame, textvariable=self.test27Text,command=self.test27Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test27Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test2701Cmd = Button(self.mainFrame, textvariable=self.test2701Text,command=self.test2701Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test2701Cmd.grid(row=rowIndex,column=1,sticky='w')
    self.test2702Cmd = Button(self.mainFrame, textvariable=self.test2702Text,command=self.test2702Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test2702Cmd.grid(row=rowIndex,column=2,sticky='w')

    # Test 28
    rowIndex += 1
    self.test28Cmd = Button(self.mainFrame, textvariable=self.test28Text,command=self.test28Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test28Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test2801Cmd = Button(self.mainFrame, textvariable=self.test2801Text,command=self.test2801Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test2801Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 29
    rowIndex += 1
    self.test29Cmd = Button(self.mainFrame, textvariable=self.test29Text,command=self.test29Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test29Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test2901Cmd = Button(self.mainFrame, textvariable=self.test2901Text,command=self.test2901Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test2901Cmd.grid(row=rowIndex,column=1,sticky='w')
    self.test2902Cmd = Button(self.mainFrame, textvariable=self.test2902Text,command=self.test2902Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test2902Cmd.grid(row=rowIndex,column=2,sticky='w')

    # Test 30
    rowIndex += 1
    self.test30Cmd = Button(self.mainFrame, textvariable=self.test30Text,command=self.test30Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test30Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test3001Cmd = Button(self.mainFrame, textvariable=self.test3001Text,command=self.test3001Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test3001Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 31
    rowIndex += 1
    self.test31Cmd = Button(self.mainFrame, textvariable=self.test31Text,command=self.test31Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test31Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test3101Cmd = Button(self.mainFrame, textvariable=self.test3101Text,command=self.test3101Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test3101Cmd.grid(row=rowIndex,column=1,sticky='w')
    self.test3102Cmd = Button(self.mainFrame, textvariable=self.test3102Text,command=self.test3102Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test3102Cmd.grid(row=rowIndex,column=2,sticky='w')

    # Test 32
    rowIndex += 1
    self.test32Cmd = Button(self.mainFrame, textvariable=self.test32Text,command=self.test32Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test32Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test3201Cmd = Button(self.mainFrame, textvariable=self.test3201Text,command=self.test3201Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test3201Cmd.grid(row=rowIndex,column=1,sticky='w')
    self.test3202Cmd = Button(self.mainFrame, textvariable=self.test3202Text,command=self.test3202Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test3202Cmd.grid(row=rowIndex,column=2,sticky='w')
    self.test3203Cmd = Button(self.mainFrame, textvariable=self.test3203Text,command=self.test3203Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test3203Cmd.grid(row=rowIndex,column=3,sticky='w')

    # Test 33
    rowIndex += 1
    self.test33Cmd = Button(self.mainFrame, textvariable=self.test33Text,command=self.test33Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test33Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test3301Cmd = Button(self.mainFrame, textvariable=self.test3301Text,command=self.test3301Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test3301Cmd.grid(row=rowIndex,column=1,sticky='w')
    self.test3302Cmd = Button(self.mainFrame, textvariable=self.test3302Text,command=self.test3302Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test3302Cmd.grid(row=rowIndex,column=2,sticky='w')

    # Test 34
    rowIndex += 1
    self.test34Cmd = Button(self.mainFrame, textvariable=self.test34Text,command=self.test34Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test34Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test3401Cmd = Button(self.mainFrame, textvariable=self.test3401Text,command=self.test3401Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test3401Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 35
    rowIndex += 1
    self.test35Cmd = Button(self.mainFrame, textvariable=self.test35Text,command=self.test35Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test35Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test3501Cmd = Button(self.mainFrame, textvariable=self.test3501Text,command=self.test3501Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test3501Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 36
    rowIndex += 1
    self.test36Cmd = Button(self.mainFrame, textvariable=self.test36Text,command=self.test36Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test36Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test3601Cmd = Button(self.mainFrame, textvariable=self.test3601Text,command=self.test3601Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test3601Cmd.grid(row=rowIndex,column=1,sticky='w')
    self.test3602Cmd = Button(self.mainFrame, textvariable=self.test3602Text,command=self.test3602Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test3602Cmd.grid(row=rowIndex,column=2,sticky='w')
    self.test3603Cmd = Button(self.mainFrame, textvariable=self.test3603Text,command=self.test3603Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test3603Cmd.grid(row=rowIndex,column=3,sticky='w')
    self.test3604Cmd = Button(self.mainFrame, textvariable=self.test3604Text,command=self.test3604Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test3604Cmd.grid(row=rowIndex,column=4,sticky='w')
    self.test3605Cmd = Button(self.mainFrame, textvariable=self.test3605Text,command=self.test3605Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test3605Cmd.grid(row=rowIndex,column=5,sticky='w')

    # Test 37
    rowIndex += 1
    self.test37Cmd = Button(self.mainFrame, textvariable=self.test37Text,command=self.test37Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test37Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test3701Cmd = Button(self.mainFrame, textvariable=self.test3701Text,command=self.test3701Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test3701Cmd.grid(row=rowIndex,column=1,sticky='w')
    self.test3702Cmd = Button(self.mainFrame, textvariable=self.test3702Text,command=self.test3702Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test3702Cmd.grid(row=rowIndex,column=2,sticky='w')

    """
    self.station01Cmd = Button(self,textvariable=self.station01Text,command=self.station01Cmd__click,height=6,width=15,font=("Arial",10,"bold"))
    self.station01Cmd.grid(row=0,column=0,sticky='nsew')
    self.station02Cmd = Button(self,textvariable=self.station02Text,command=self.station02Cmd__click,width=15,font=("Arial",10,"bold"))
    self.station02Cmd.grid(row=0,column=1,sticky='nsew')
    self.station03Cmd = Button(self,textvariable=self.station03Text,command=self.station03Cmd__click,width=15,font=("Arial",10,"bold"))
    self.station03Cmd.grid(row=0,column=2,sticky='nsew')
    self.station04Cmd = Button(self,textvariable=self.station04Text,command=self.station04Cmd__click,width=15,font=("Arial",10,"bold"))
    self.station04Cmd.grid(row=0,column=3,sticky='nsew')
    self.station05Cmd = Button(self,textvariable=self.station05Text,command=self.station05Cmd__click,width=15,font=("Arial",10,"bold"))
    self.station05Cmd.grid(row=0,column=4,sticky='nsew')
    self.station06Cmd = Button(self,textvariable=self.station06Text,command=self.station06Cmd__click,height=6,width=15,font=("Arial",10,"bold"))
    self.station06Cmd.grid(row=1,column=0,sticky='nsew')
    self.station07Cmd = Button(self,textvariable=self.station07Text,command=self.station07Cmd__click,width=15,font=("Arial",10,"bold"))
    self.station07Cmd.grid(row=1,column=1,sticky='nsew')
    self.station08Cmd = Button(self,textvariable=self.station08Text,command=self.station08Cmd__click,font=("Arial",10,"bold"))
    self.station08Cmd.grid(row=1,column=2,sticky='nsew')
    self.station09Cmd = Button(self,textvariable=self.station09Text,command=self.station09Cmd__click,font=("Arial",10,"bold"))
    self.station09Cmd.grid(row=1,column=3,sticky='nsew')
    self.station10Cmd = Button(self,textvariable=self.station10Text,command=self.station10Cmd__click,font=("Arial",10,"bold"))
    self.station10Cmd.grid(row=1,column=4,sticky='nsew')
    self.station11Cmd = Button(self,textvariable=self.station11Text,command=self.station11Cmd__click,height=6,font=("Arial",10,"bold"))
    self.station11Cmd.grid(row=2,column=0,sticky='nsew')
    self.station12Cmd = Button(self,textvariable=self.station12Text,command=self.station12Cmd__click,font=("Arial",10,"bold"))
    self.station12Cmd.grid(row=2,column=1,sticky='nsew')
    self.station13Cmd = Button(self,textvariable=self.station13Text,command=self.station13Cmd__click,font=("Arial",10,"bold"))
    self.station13Cmd.grid(row=2,column=2,sticky='nsew')
    self.station14Cmd = Button(self,textvariable=self.station14Text,command=self.station14Cmd__click,font=("Arial",10,"bold"))
    self.station14Cmd.grid(row=2,column=3,sticky='nsew')
    self.station15Cmd = Button(self,textvariable=self.station15Text,command=self.station15Cmd__click,font=("Arial",10,"bold"))
    self.station15Cmd.grid(row=2,column=4,sticky='nsew')
    self.station16Cmd = Button(self,textvariable=self.station16Text,command=self.station16Cmd__click,height=6,bg="white",font=("Arial",10,"bold"))
    self.station16Cmd.grid(row=3,column=0,sticky='nsew')
    self.station17Cmd = Button(self,textvariable=self.station17Text,command=self.station17Cmd__click,bg="yellow",font=("Arial",10,"bold"))
    self.station17Cmd.grid(row=3,column=1,sticky='nsew')
    self.station18Cmd = Button(self,textvariable=self.station18Text,command=self.station18Cmd__click,bg="cyan",font=("Arial",10,"bold"))
    self.station18Cmd.grid(row=3,column=2,sticky='nsew')
    self.station19Cmd = Button(self,textvariable=self.station19Text,command=self.station19Cmd__click,fg="white",bg="black",font=("Arial",10,"bold"))
    self.station19Cmd.grid(row=3,column=3,sticky='nsew')
    self.station20Cmd = Button(self,textvariable=self.station20Text,command=self.station20Cmd__click,font=("Arial",10,"bold"))
    self.station20Cmd.grid(row=3,column=4,sticky='nsew')
    self.resetButtonColours()
    """
  def resetContLabels(self):
    self.test01Cmd["bg"] = "grey"
    self.test0101Cmd["bg"] = "grey"

    self.test02Cmd["bg"] = "grey"
    self.test0201Cmd["bg"] = "grey"
    self.test0202Cmd["bg"] = "grey"
    self.test0203Cmd["bg"] = "grey"
    self.test0204Cmd["bg"] = "grey"
    self.test0205Cmd["bg"] = "grey"
    self.test0206Cmd["bg"] = "grey"
    self.test0207Cmd["bg"] = "grey"
    self.test0208Cmd["bg"] = "grey"
    self.test0209Cmd["bg"] = "grey"


    self.test03Cmd["bg"] = "grey"
    self.test0301Cmd["bg"] = "grey"

    self.test04Cmd["bg"] = "grey"
    self.test0401Cmd["bg"] = "grey"
    self.test0402Cmd["bg"] = "grey"
    self.test0403Cmd["bg"] = "grey"
    self.test0404Cmd["bg"] = "grey"
    self.test0405Cmd["bg"] = "grey"
    self.test0406Cmd["bg"] = "grey"

    self.test05Cmd["bg"] = "grey"
    self.test0501Cmd["bg"] = "grey"

    self.test06Cmd["bg"] = "grey"
    self.test0601Cmd["bg"] = "grey"
    self.test0602Cmd["bg"] = "grey"

    self.test07Cmd["bg"] = "grey"
    self.test0701Cmd["bg"] = "grey"

    self.test08Cmd["bg"] = "grey"
    self.test0801Cmd["bg"] = "grey"
    self.test0802Cmd["bg"] = "grey"

    self.test09Cmd["bg"] = "grey"
    self.test0901Cmd["bg"] = "grey"

    self.test10Cmd["bg"] = "grey"
    self.test1001Cmd["bg"] = "grey"

    self.test11Cmd["bg"] = "grey"
    self.test1101Cmd["bg"] = "grey"
    self.test1102Cmd["bg"] = "grey"
    self.test1103Cmd["bg"] = "grey"

    self.test12Cmd["bg"] = "grey"
    self.test1201Cmd["bg"] = "grey"

    self.test13Cmd["bg"] = "grey"
    self.test1301Cmd["bg"] = "grey"

    self.test14Cmd["bg"] = "grey"
    self.test1401Cmd["bg"] = "grey"
    self.test1402Cmd["bg"] = "grey"
    self.test1403Cmd["bg"] = "grey"

    self.test15Cmd["bg"] = "grey"
    self.test1501Cmd["bg"] = "grey"
    self.test1502Cmd["bg"] = "grey"
    self.test1503Cmd["bg"] = "grey"

    self.test16Cmd["bg"] = "grey"
    self.test1601Cmd["bg"] = "grey"

    self.test17Cmd["bg"] = "grey"
    self.test1701Cmd["bg"] = "grey"

    self.test18Cmd["bg"] = "grey"
    self.test1801Cmd["bg"] = "grey"

    self.test19Cmd["bg"] = "grey"
    self.test1901Cmd["bg"] = "grey"

    self.test20Cmd["bg"] = "grey"
    self.test2001Cmd["bg"] = "grey"

    self.test21Cmd["bg"] = "grey"
    self.test2101Cmd["bg"] = "grey"

    self.test22Cmd["bg"] = "grey"
    self.test2201Cmd["bg"] = "grey"

    self.test23Cmd["bg"] = "grey"
    self.test2301Cmd["bg"] = "grey"

    self.test24Cmd["bg"] = "grey"
    self.test2401Cmd["bg"] = "grey"

    self.test25Cmd["bg"] = "grey"
    self.test2501Cmd["bg"] = "grey"
    self.test2502Cmd["bg"] = "grey"

    self.test26Cmd["bg"] = "grey"
    self.test2601Cmd["bg"] = "grey"

    self.test27Cmd["bg"] = "grey"
    self.test2701Cmd["bg"] = "grey"
    self.test2702Cmd["bg"] = "grey"

    self.test28Cmd["bg"] = "grey"
    self.test2801Cmd["bg"] = "grey"

    self.test29Cmd["bg"] = "grey"
    self.test2901Cmd["bg"] = "grey"
    self.test2902Cmd["bg"] = "grey"

    self.test30Cmd["bg"] = "grey"
    self.test3001Cmd["bg"] = "grey"

    self.test31Cmd["bg"] = "grey"
    self.test3101Cmd["bg"] = "grey"
    self.test3102Cmd["bg"] = "grey"

    self.test32Cmd["bg"] = "grey"
    self.test3201Cmd["bg"] = "grey"
    self.test3202Cmd["bg"] = "grey"
    self.test3203Cmd["bg"] = "grey"

    self.test33Cmd["bg"] = "grey"
    self.test3301Cmd["bg"] = "grey"
    self.test3302Cmd["bg"] = "grey"

    self.test34Cmd["bg"] = "grey"
    self.test3401Cmd["bg"] = "grey"

    self.test35Cmd["bg"] = "grey"
    self.test3501Cmd["bg"] = "grey"

    self.test36Cmd["bg"] = "grey"
    self.test3601Cmd["bg"] = "grey"
    self.test3602Cmd["bg"] = "grey"
    self.test3603Cmd["bg"] = "grey"
    self.test3604Cmd["bg"] = "grey"
    self.test3605Cmd["bg"] = "grey"

    self.test37Cmd["bg"] = "grey"
    self.test3701Cmd["bg"] = "grey"
    self.test3702Cmd["bg"] = "grey"

    # Frame 2
    self.test201Cmd["bg"] = "grey"
    self.test20101Cmd["bg"] = "grey"

    self.test202Cmd["bg"] = "grey"
    self.test20201Cmd["bg"] = "grey"
    self.test20202Cmd["bg"] = "grey"
    self.test20203Cmd["bg"] = "grey"
    self.test20204Cmd["bg"] = "grey"
    self.test20205Cmd["bg"] = "grey"
    self.test20206Cmd["bg"] = "grey"
    self.test20207Cmd["bg"] = "grey"
    self.test20208Cmd["bg"] = "grey"

    self.test203Cmd["bg"] = "grey"
    self.test20301Cmd["bg"] = "grey"

    self.test204Cmd["bg"] = "grey"
    self.test20401Cmd["bg"] = "grey"
    self.test20402Cmd["bg"] = "grey"
    self.test20403Cmd["bg"] = "grey"
    self.test20404Cmd["bg"] = "grey"
    self.test20405Cmd["bg"] = "grey"
    self.test20406Cmd["bg"] = "grey"

    self.test205Cmd["bg"] = "grey"
    self.test20501Cmd["bg"] = "grey"

    self.test206Cmd["bg"] = "grey"
    self.test20601Cmd["bg"] = "grey"

    self.test207Cmd["bg"] = "grey"
    self.test20701Cmd["bg"] = "grey"

    self.test208Cmd["bg"] = "grey"
    self.test20801Cmd["bg"] = "grey"

    self.test209Cmd["bg"] = "grey"
    self.test20901Cmd["bg"] = "grey"

    self.test210Cmd["bg"] = "grey"
    self.test21001Cmd["bg"] = "grey"

    self.test211Cmd["bg"] = "grey"
    self.test21101Cmd["bg"] = "grey"
    self.test21102Cmd["bg"] = "grey"
    self.test21103Cmd["bg"] = "grey"

    self.test212Cmd["bg"] = "grey"
    self.test21201Cmd["bg"] = "grey"
    self.test21202Cmd["bg"] = "grey"
    self.test21203Cmd["bg"] = "grey"

    self.test213Cmd["bg"] = "grey"
    self.test21301Cmd["bg"] = "grey"
    self.test21302Cmd["bg"] = "grey"
    self.test21303Cmd["bg"] = "grey"

    self.test214Cmd["bg"] = "grey"
    self.test21401Cmd["bg"] = "grey"
    self.test21402Cmd["bg"] = "grey"
    self.test21403Cmd["bg"] = "grey"

    self.test215Cmd["bg"] = "grey"
    self.test21501Cmd["bg"] = "grey"

    self.test216Cmd["bg"] = "grey"
    self.test21601Cmd["bg"] = "grey"

    self.test217Cmd["bg"] = "grey"
    self.test21701Cmd["bg"] = "grey"

    self.test218Cmd["bg"] = "grey"
    self.test21801Cmd["bg"] = "grey"

    self.test219Cmd["bg"] = "grey"
    self.test21901Cmd["bg"] = "grey"

    self.test220Cmd["bg"] = "grey"
    self.test22001Cmd["bg"] = "grey"
    self.test22002Cmd["bg"] = "grey"
    self.test22003Cmd["bg"] = "grey"
#    self.test22004Cmd["bg"] = "grey"
 #   self.test22005Cmd["bg"] = "grey"

    self.test221Cmd["bg"] = "grey"
    self.test22101Cmd["bg"] = "grey"

    self.test222Cmd["bg"] = "grey"
    self.test22201Cmd["bg"] = "grey"

    self.test223Cmd["bg"] = "grey"
    self.test22301Cmd["bg"] = "grey"

    self.test224Cmd["bg"] = "grey"
    self.test22401Cmd["bg"] = "grey"
    self.test22402Cmd["bg"] = "grey"
    self.test22403Cmd["bg"] = "grey"


    print("Reset cont labels")

  # Start/Stop
  def test00Cmd__click(self):
    print("<TEST ALL>")
    if self.testingAll:
      return

    # Reset label colours
    self.resetContLabels()

#    if self.testPart == "4569":
#      self.station17Cmd__click()
#    else:
#      self.station16Cmd__click()
    self.abortSignal = False
    self.testingAll = True


    self.test01Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.test02Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.test03Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.test04Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.test05Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.test06Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.test07Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.test08Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.test09Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.test10Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.test11Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.test12Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.test13Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.test14Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.test15Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.test16Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.test17Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.test18Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.test19Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.test20Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.test21Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.test22Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.test23Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.test24Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.test25Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.test26Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.test27Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.test28Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.test29Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.test30Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.test31Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.test32Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.test33Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.test34Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.test35Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.test36Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.test37Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.testingAll = False
    self.abortSignal = False


    print("test00")
    #exit()

  def test0001Cmd__click(self):
    self.abortSignal = True
    if self.testingAll:
      return
    self.resetContLabels()
    print("test0001")
    #exit()
  # Test 1

  def test0002Cmd__click(self):
    if self.testingAll:
      return
    self.resetContLabels()
    self.mainCanvas.pack_forget()
    self.main2Canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
    self.canvasScroll.config(command=self.main2Canvas.yview)

  def test0003Cmd__click(self):
    os.system("sudo shutdown now")

    print("test0001")

##  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
##  <<< Start of Frame 2 >>>
##  @@@@@@@@@@@@@@@@@@@@@@@@@
  # Start/Stop
  def test200Cmd__click(self):
    print("<TEST ALL>")
    if self.testingAll:
      return

    # Reset label colours
    self.resetContLabels()
    self.abortSignal = False
    self.testingAll = True


    self.test201Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.test202Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.test203Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.test204Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.test205Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.test206Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.test207Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.test208Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.test209Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.test210Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.test211Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.test212Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.test213Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.test214Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.test215Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.test216Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.test217Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.test218Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.test219Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.test220Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.test221Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.test222Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.test223Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return
    self.test224Cmd__click()
    self.update()
    if self.abortSignal or self.GT1000.GT_Abort:
      self.testingAll = False
      self.abortSignal = False
      return

    self.testingAll = False
    self.abortSignal = False


  def test20002Cmd__click(self):
    if self.testingAll:
      return
    self.resetContLabels()
    self.main2Canvas.pack_forget()
    self.mainCanvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
    self.canvasScroll.config(command=self.mainCanvas.yview)


  def test20001Cmd__click(self):
    self.abortSignal = True
    if self.testingAll:
      return
    self.resetContLabels()
    print("test0001")
    #exit()

  # Test 1
  def test201Cmd__click(self):
    self.GT1000.clear_outputs()
    tChip = 0x39
    tPin = 0x04
    rPin = 1

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.S1X[rPin]:
      self.test20101Cmd["bg"] = "green"
      self.test20101Cmd["activebackground"] = "green"
    else:
      self.test20101Cmd["bg"] = "red"
      self.test20101Cmd["activebackground"] = "red"
#    exit()

  def test20101Cmd__click(self):
    print("test20101")

  # Test 2
  def test202Cmd__click(self):
    print("test202")
    self.GT1000.clear_outputs()
    tChip = 0x39
    tPin = 0x08
    rPin = 1

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.GND[1]:
      self.test20201Cmd["bg"] = "green"
      self.test20201Cmd["activebackground"] = "green"
    else:
      self.test20201Cmd["bg"] = "red"
      self.test20201Cmd["activebackground"] = "red"
    if self.GT1000.GND[2]:
      self.test20202Cmd["bg"] = "green"
      self.test20202Cmd["activebackground"] = "green"
    else:
      self.test20202Cmd["bg"] = "red"
      self.test20202Cmd["activebackground"] = "red"
    if self.GT1000.GND[3]:
      self.test20203Cmd["bg"] = "green"
      self.test20203Cmd["activebackground"] = "green"
    else:
      self.test20203Cmd["bg"] = "red"
      self.test20203Cmd["activebackground"] = "red"
    if self.GT1000.GND[4]:
      self.test20204Cmd["bg"] = "green"
      self.test20204Cmd["activebackground"] = "green"
    else:
      self.test20204Cmd["bg"] = "red"
      self.test20204Cmd["activebackground"] = "red"
    if self.GT1000.GND[5]:
      self.test20205Cmd["bg"] = "green"
      self.test20205Cmd["activebackground"] = "green"
    else:
      self.test20205Cmd["bg"] = "red"
      self.test20205Cmd["activebackground"] = "red"
    if self.GT1000.GND[6]:
      self.test20206Cmd["bg"] = "green"
      self.test20206Cmd["activebackground"] = "green"
    else:
      self.test20206Cmd["bg"] = "red"
      self.test20206Cmd["activebackground"] = "red"
    if self.GT1000.GND[7]:
      self.test20207Cmd["bg"] = "green"
      self.test20207Cmd["activebackground"] = "green"
    else:
      self.test20207Cmd["bg"] = "red"
      self.test20207Cmd["activebackground"] = "red"
    if self.GT1000.GND[8]:
      self.test20208Cmd["bg"] = "green"
      self.test20208Cmd["activebackground"] = "green"
    else:
      self.test20208Cmd["bg"] = "red"
      self.test20208Cmd["activebackground"] = "red"





  def test20201Cmd__click(self):
    print("test20201")
  def test20202Cmd__click(self):
    print("test20202")
  def test20203Cmd__click(self):
    print("test20203")
  def test20204Cmd__click(self):
    print("test20204")
  def test20205Cmd__click(self):
    print("test20205")
  def test20206Cmd__click(self):
    print("test20206")
  def test20207Cmd__click(self):
    print("test20207")
  def test20208Cmd__click(self):
    print("test20208")

  # Test 3
  def test203Cmd__click(self):
    print("test203")
    self.GT1000.clear_outputs()
    tChip = 0x39
    tPin = 0x10
    rPin = 2

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.S1X[2]:
      self.test20301Cmd["bg"] = "green"
      self.test20301Cmd["activebackground"] = "green"
    else:
      self.test20301Cmd["bg"] = "red"
      self.test20301Cmd["activebackground"] = "red"
    #exit()
  def test20301Cmd__click(self):
    print("test20301")

  # Test 4
  def test204Cmd__click(self):
    print("test204")
    self.GT1000.clear_outputs()
    tChip = 0x39
    tPin = 0x80
    rPin = 0

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.HELMET[1]:
      self.test20401Cmd["bg"] = "green"
      self.test20401Cmd["activebackground"] = "green"
    else:
      self.test20401Cmd["bg"] = "red"
      self.test20401Cmd["activebackground"] = "red"
    if self.GT1000.PARTICULE[1]:
      self.test20402Cmd["bg"] = "green"
      self.test20402Cmd["activebackground"] = "green"
    else:
      self.test20402Cmd["bg"] = "red"
      self.test20402Cmd["activebackground"] = "red"
    if self.GT1000.POSTNEG:
      self.test20403Cmd["bg"] = "green"
      self.test20403Cmd["activebackground"] = "green"
    else:
      self.test20403Cmd["bg"] = "red"
      self.test20403Cmd["activebackground"] = "red"
    if self.GT1000.CHASE_1[2]:
      self.test20404Cmd["bg"] = "green"
      self.test20404Cmd["activebackground"] = "green"
    else:
      self.test20404Cmd["bg"] = "red"
      self.test20404Cmd["activebackground"] = "red"
    if self.GT1000.CHASE_2[2]:
      self.test20405Cmd["bg"] = "green"
      self.test20405Cmd["activebackground"] = "green"
    else:
      self.test20405Cmd["bg"] = "red"
      self.test20405Cmd["activebackground"] = "red"
    if self.GT1000.CHASE_3[2]:
      self.test20406Cmd["bg"] = "green"
      self.test20406Cmd["activebackground"] = "green"
    else:
      self.test20406Cmd["bg"] = "red"
      self.test20406Cmd["activebackground"] = "red"




    #exit()
  def test20401Cmd__click(self):
    print("test20401")
  def test20402Cmd__click(self):
    print("test20402")
  def test20403Cmd__click(self):
    print("test20403")
  def test20404Cmd__click(self):
    print("test20404")
  def test20405Cmd__click(self):
    print("test20405")
  def test20406Cmd__click(self):
    print("test20406")

  # Test 5
  def test205Cmd__click(self):
    print("test205")
    self.GT1000.clear_outputs()
    tChip = 0x39
    tPin = 0x20
    rPin = 0x01

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.AFB2[8]:
      self.test20501Cmd["bg"] = "green"
      self.test20501Cmd["activebackground"] = "green"
    else:
      self.test20501Cmd["bg"] = "red"
      self.test20501Cmd["activebackground"] = "red"
    #exit()
  def test20501Cmd__click(self):
    print("test20501")

  # Test 6
  def test206Cmd__click(self):
    print("test206")
    self.GT1000.clear_outputs()
    tChip = 0x38
    tPin = 0x08
    rPin = 0x01

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.SXX[1]:
      self.test20601Cmd["bg"] = "green"
      self.test20601Cmd["activebackground"] = "green"
    else:
      self.test20601Cmd["bg"] = "red"
      self.test20601Cmd["activebackground"] = "red"
    #exit()
  def test20601Cmd__click(self):
    print("test20601")

  # Test 7
  def test207Cmd__click(self):
    print("test207")
    self.GT1000.clear_outputs()
    tChip = 0x38
    tPin = 0x10
    rPin = 0x01

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.SXX[2]:
      self.test20701Cmd["bg"] = "green"
      self.test20701Cmd["activebackground"] = "green"
    else:
      self.test20701Cmd["bg"] = "red"
      self.test20701Cmd["activebackground"] = "red"
    #exit()
  def test20701Cmd__click(self):
    print("test20701")

  # Test 8
  def test208Cmd__click(self):
    print("test208")
    self.GT1000.clear_outputs()
    tChip = 0x38
    tPin = 0x80
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.SXX[3]:
      self.test20801Cmd["bg"] = "green"
      self.test20801Cmd["activebackground"] = "green"
    else:
      self.test20801Cmd["bg"] = "red"
      self.test20801Cmd["activebackground"] = "red"
    #exit()
  def test20801Cmd__click(self):
    print("test20801")

  # Test 9
  def test209Cmd__click(self):
    print("test209")
    self.GT1000.clear_outputs()
    tChip = 0x38
    tPin = 0x20
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.PARTICULE[3]:
      self.test20901Cmd["bg"] = "green"
      self.test20901Cmd["activebackground"] = "green"
    else:
      self.test20901Cmd["bg"] = "red"
      self.test20901Cmd["activebackground"] = "red"
    #exit()
  def test20901Cmd__click(self):
    print("test20901")

  # Test 10
  def test210Cmd__click(self):
    print("test210")
    self.GT1000.clear_outputs()
    tChip = 0x38
    tPin = 0x40
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.HELMET[3]:
      self.test21001Cmd["bg"] = "green"
      self.test21001Cmd["activebackground"] = "green"
    else:
      self.test21001Cmd["bg"] = "red"
      self.test21001Cmd["activebackground"] = "red"
    #exit()
  def test21001Cmd__click(self):
    print("test21001")

  # Test 11
  def test211Cmd__click(self):
    print("test211")
    self.GT1000.clear_outputs()
    tChip = 0x38
    tPin = 0x01
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.CHASE_1[6]:
      self.test21101Cmd["bg"] = "green"
      self.test21101Cmd["activebackground"] = "green"
    else:
      self.test21101Cmd["bg"] = "red"
      self.test21101Cmd["activebackground"] = "red"
    if self.GT1000.CHASE_2[6]:
      self.test21102Cmd["bg"] = "green"
      self.test21102Cmd["activebackground"] = "green"
    else:
      self.test21102Cmd["bg"] = "red"
      self.test21102Cmd["activebackground"] = "red"
    if self.GT1000.CHASE_3[6]:
      self.test21103Cmd["bg"] = "green"
      self.test21103Cmd["activebackground"] = "green"
    else:
      self.test21103Cmd["bg"] = "red"
      self.test21103Cmd["activebackground"] = "red"
    #exit(
  def test21101Cmd__click(self):
    print("test21101")
  def test21102Cmd__click(self):
    print("test21102")
  def test21103Cmd__click(self):
    print("test21103")

  # Test 12
  def test212Cmd__click(self):
    print("test212")
    self.GT1000.clear_outputs()
    tChip = 0x3A
    tPin = 0x04
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.CHASE_1[4]:
      self.test21201Cmd["bg"] = "green"
      self.test21201Cmd["activebackground"] = "green"
    else:
      self.test21201Cmd["bg"] = "red"
      self.test21201Cmd["activebackground"] = "red"
    if self.GT1000.CHASE_2[4]:
      self.test21202Cmd["bg"] = "green"
      self.test21202Cmd["activebackground"] = "green"
    else:
      self.test21202Cmd["bg"] = "red"
      self.test21202Cmd["activebackground"] = "red"
    if self.GT1000.CHASE_2[4]:
      self.test21203Cmd["bg"] = "green"
      self.test21203Cmd["activebackground"] = "green"
    else:
      self.test21203Cmd["bg"] = "red"
      self.test21203Cmd["activebackground"] = "red"
    #exit()
  def test21201Cmd__click(self):
    print("test21201")
  def test21202Cmd__click(self):
    print("test21202")
  def test21203Cmd__click(self):
    print("test21203")

  # Test 13
  def test213Cmd__click(self):
    print("test213")
    self.GT1000.clear_outputs()
    tChip = 0x3A
    tPin = 0x08
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.CHASE_1[5]:
      self.test21301Cmd["bg"] = "green"
      self.test21301Cmd["activebackground"] = "green"
    else:
      self.test21301Cmd["bg"] = "red"
      self.test21301Cmd["activebackground"] = "red"
    if self.GT1000.CHASE_2[5]:
      self.test21302Cmd["bg"] = "green"
      self.test21302Cmd["activebackground"] = "green"
    else:
      self.test21302Cmd["bg"] = "red"
      self.test21302Cmd["activebackground"] = "red"
    if self.GT1000.CHASE_3[5]:
      self.test21303Cmd["bg"] = "green"
      self.test21303Cmd["activebackground"] = "green"
    else:
      self.test21303Cmd["bg"] = "red"
      self.test21303.Cmd["activebackground"] = "red"
    #exit()
  def test21301Cmd__click(self):
    print("test21301")
  def test21302Cmd__click(self):
    print("test21302")
  def test21303Cmd__click(self):
    print("test21303")

  # Test 14
  def test214Cmd__click(self):
    print("test214")
    self.GT1000.clear_outputs()
    tChip = 0x3A
    tPin = 0x10
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.CHASE_1[3]:
      self.test21401Cmd["bg"] = "green"
      self.test21401Cmd["activebackground"] = "green"
    else:
      self.test21401Cmd["bg"] = "red"
      self.test21401Cmd["activebackground"] = "red"
    if self.GT1000.CHASE_2[3]:
      self.test21402Cmd["bg"] = "green"
      self.test21402Cmd["activebackground"] = "green"
    else:
      self.test21402Cmd["bg"] = "red"
      self.test21402Cmd["activebackground"] = "red"
    if self.GT1000.CHASE_3[3]:
      self.test21403Cmd["bg"] = "green"
      self.test21403Cmd["activebackground"] = "green"
    else:
      self.test21403Cmd["bg"] = "red"
      self.test21403Cmd["activebackground"] = "red"
    #exit()
  def test21401Cmd__click(self):
    print("test21401")
  def test21402Cmd__click(self):
    print("test21402")
  def test21403Cmd__click(self):
    print("test21403")

  # Test 15
  def test215Cmd__click(self):
    print("test215")
    self.GT1000.clear_outputs()
    tChip = 0x3A
    tPin = 0x02
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.SXX[4]:
      self.test21501Cmd["bg"] = "green"
      self.test21501Cmd["activebackground"] = "green"
    else:
      self.test21501Cmd["bg"] = "red"
      self.test21501Cmd["activebackground"] = "red"

    #exit()
  def test21501Cmd__click(self):
    print("test21501")

  # Test 16
  def test216Cmd__click(self):
    print("test216")
    self.GT1000.clear_outputs()
    tChip = 0x3C
    tPin = 0x10
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.SXX[5]:
      self.test21601Cmd["bg"] = "green"
      self.test21601Cmd["activebackground"] = "green"
    else:
      self.test21601Cmd["bg"] = "red"
      self.test21601Cmd["activebackground"] = "red"
    #exit()
  def test21601Cmd__click(self):
    print("test21601")

  # Test 17
  def test217Cmd__click(self):
    print("test217")
    self.GT1000.clear_outputs()
    tChip = 0x3C
    tPin = 0x20
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.SXX[6]:
      self.test21701Cmd["bg"] = "green"
      self.test21701Cmd["activebackground"] = "green"
    else:
      self.test21701Cmd["bg"] = "red"
      self.test21701Cmd["activebackground"] = "red"
    #exit()
  def test21701Cmd__click(self):
    print("test21701")

  # Test 18
  def test218Cmd__click(self):
    print("test218")
    self.GT1000.clear_outputs()
    tChip = 0x3C
    tPin = 0x40
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.SXX[7]:
      self.test21801Cmd["bg"] = "green"
      self.test21801Cmd["activebackground"] = "green"
    else:
      self.test21801Cmd["bg"] = "red"
      self.test21801Cmd["activebackground"] = "red"
    #exit()
  def test21801Cmd__click(self):
    print("test21801")

  # Test 19
  def test219Cmd__click(self):
    print("test219")
    self.GT1000.clear_outputs()
    tChip = 0x3C
    tPin = 0x80
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.SXX[8]:
      self.test21901Cmd["bg"] = "green"
      self.test21901Cmd["activebackground"] = "green"
    else:
      self.test21901Cmd["bg"] = "red"
      self.test21901Cmd["activebackground"] = "red"
    #exit()
  def test21901Cmd__click(self):
    print("test21901")

  # Test 20
  def test220Cmd__click(self):
    print("test220")
    self.GT1000.clear_outputs()
    tChip = 0x3C
    tPin = 0x01
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.CHASE_1[1]:
      self.test22001Cmd["bg"] = "green"
      self.test22001Cmd["activebackground"] = "green"
    else:
      self.test22001Cmd["bg"] = "red"
      self.test22001Cmd["activebackground"] = "red"
    if self.GT1000.CHASE_2[1]:
      self.test22002Cmd["bg"] = "green"
      self.test22002Cmd["activebackground"] = "green"
    else:
      self.test22002Cmd["bg"] = "red"
      self.test22002Cmd["activebackground"] = "red"
    if self.GT1000.CHASE_3[1]:
      self.test22003Cmd["bg"] = "green"
      self.test22003Cmd["activebackground"] = "green"
    else:
      self.test22003Cmd["bg"] = "red"
      self.test22003Cmd["activebackground"] = "red"
    #exit()
  def test22001Cmd__click(self):
    print("test22001")
  def test22002Cmd__click(self):
    print("test22002")
  def test22003Cmd__click(self):
    print("test22003")
  def test22004Cmd__click(self):
    print("test22004")
  def test22005Cmd__click(self):
    print("test22005")

  # Test 21
  def test221Cmd__click(self):
    print("test221")
    self.GT1000.clear_outputs()
    tChip = 0x3C
    tPin = 0x02
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.HELMET[2]:
      self.test22101Cmd["bg"] = "green"
      self.test22101Cmd["activebackground"] = "green"
    else:
      self.test22101Cmd["bg"] = "red"
      self.test22101Cmd["activebackground"] = "red"
    #exit()
  def test22101Cmd__click(self):
    print("test22101")

  # Test 22
  def test222Cmd__click(self):
    print("test222")
    self.GT1000.clear_outputs()
    tChip = 0x3C
    tPin = 0x04
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.PARTICULE[2]:
      self.test22201Cmd["bg"] = "green"
      self.test22201Cmd["activebackground"] = "green"
    else:
      self.test22201Cmd["bg"] = "red"
      self.test22201Cmd["activebackground"] = "red"
    #exit()
  def test22201Cmd__click(self):
    print("test22201")

  # Test 23
  def test223Cmd__click(self):
    print("test223")
    self.GT1000.clear_outputs()
    tChip = 0x3D
    tPin = 0x02
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.AFB2[7]:
      self.test22301Cmd["bg"] = "green"
      self.test22301Cmd["activebackground"] = "green"
    else:
      self.test22301Cmd["bg"] = "red"
      self.test22301Cmd["activebackground"] = "red"
    #exit()
  def test22301Cmd__click(self):
    print("test22301")

  # Test 24
  def test224Cmd__click(self):
    print("test224")
    self.GT1000.clear_outputs()
    tChip = 0x3D
    tPin = 0x01
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.AFB2[2]:
      self.test22401Cmd["bg"] = "green"
      self.test22401Cmd["activebackground"] = "green"
    else:
      self.test22401Cmd["bg"] = "red"
      self.test22401Cmd["activebackground"] = "red"
    if self.GT1000.AFB2[4]:
      self.test22402Cmd["bg"] = "green"
      self.test22402Cmd["activebackground"] = "green"
    else:
      self.test22402Cmd["bg"] = "red"
      self.test22402Cmd["activebackground"] = "red"
    if self.GT1000.AFB2[5]:
      self.test22403Cmd["bg"] = "green"
      self.test22403Cmd["activebackground"] = "green"
    else:
      self.test22403Cmd["bg"] = "red"
      self.test22403Cmd["activebackground"] = "red"
    #exit()
  def test22401Cmd__click(self):
    print("test22401")
  def test22402Cmd__click(self):
    print("test22402")
  def test22403Cmd__click(self):
    print("test22403")


#  def test201Cmd__click(self):
#    self.GT1000.clear_outputs()
#    tChip = 0x39
#    tPin = 0x04
#    rPin = 27

#    print("Output to ACM1.1, expect AFB1.E3")
#    self.GT1000.setBankByPin(16)
#    time.sleep(30/1000)
#    self.GT1000.write_output(tChip,tPin)
#    if self.GT1000.AFB1[rPin]:
#      self.test20101Cmd["bg"] = "green"
#      self.test20101Cmd["activebackground"] = "green"
#    else:
#      self.test20101Cmd["bg"] = "red"
#      self.test20101Cmd["activebackground"] = "red"
#    exit()
#
#  def test20101Cmd__click(self):
#    print("test20101")#
#
#  def test20102Cmd__click(self):
#    print("test20102")
#
#  def test20103Cmd__click(self):
#    print("test20103")
#
#  def test204Cmd__click(self):
#    self.GT1000.clear_outputs()
#    self.resetContLabels()
#    tChip = 0x39
#    tPin = 0x04
#    rPin = 27#
#
#    print("Output to ACM1.1, expect AFB1.E3")
#    self.GT1000.setBankByPin(16)
#    time.sleep(30/1000)
#    self.GT1000.write_output(tChip,tPin)
#    if self.GT1000.AFB1[rPin]:
#      self.test20401Cmd["bg"] = "green"
#      self.test20401Cmd["activebackground"] = "green"
#    else:
#      self.test20401Cmd["bg"] = "red"
#      self.test20401Cmd["activebackground"] = "red"
##    exit()#
#
#  def test20401Cmd__click(self):
#    print("test20401")
#  def test20402Cmd__click(self):
#    print("test20402")
#  def test20403Cmd__click(self):
#    print("tesy20403")
#  def test20404Cmd__click(self):
#    print("test20404")
#  def test20405Cmd__click(self):
#    print("test20405")
#  def test20406Cmd__click(self):
#    print("test20406")#

##   &&&&&&&&&&&&&&&&&&&&&&&
##  <<< Start of Original >>>
##   &&&&&&&&&&&&&&&&&&&&&&&


  def test01Cmd__click(self):
    self.GT1000.clear_outputs()
    tChip = 0x39
    tPin = 0x04
    rPin = 27

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.AFB1[rPin]:
      self.test0101Cmd["bg"] = "green"
      self.test0101Cmd["activebackground"] = "green"
    else:
      self.test0101Cmd["bg"] = "red"
      self.test0101Cmd["activebackground"] = "red"
#    exit()

  def test0101Cmd__click(self):
    print("test0101")

  # Test 2
  def test02Cmd__click(self):
    print("test02")
    self.GT1000.clear_outputs()
    tChip = 0x39
    tPin = 0x08
    rPin = 1

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.LED_L[1]:
      self.test0201Cmd["bg"] = "green"
      self.test0201Cmd["activebackground"] = "green"
    else:
      self.test0201Cmd["bg"] = "red"
      self.test0201Cmd["activebackground"] = "red"
    if self.GT1000.LED_R[1]:
      self.test0202Cmd["bg"] = "green"
      self.test0202Cmd["activebackground"] = "green"
    else:
      self.test0202Cmd["bg"] = "red"
      self.test0202Cmd["activebackground"] = "red"
    if self.GT1000.POSTNEG:
      self.test0203Cmd["bg"] = "green"
      self.test0203Cmd["activebackground"] = "green"
    else:
      self.test0203Cmd["bg"] = "red"
      self.test0203Cmd["activebackground"] = "red"
    if self.GT1000.WIPER[1]:
      self.test0204Cmd["bg"] = "green"
      self.test0204Cmd["activebackground"] = "green"
    else:
      self.test0204Cmd["bg"] = "red"
      self.test0204Cmd["activebackground"] = "red"
    if self.GT1000.SW_1[7]:
      self.test0205Cmd["bg"] = "green"
      self.test0205Cmd["activebackground"] = "green"
    else:
      self.test0205Cmd["bg"] = "red"
      self.test0205Cmd["activebackground"] = "red"
    if self.GT1000.LED_HOOD[1]:
      self.test0206Cmd["bg"] = "green"
      self.test0206Cmd["activebackground"] = "green"
    else:
      self.test0206Cmd["bg"] = "red"
      self.test0206Cmd["activebackground"] = "red"
    if self.GT1000.LED_BUMPER[2]:
      self.test0207Cmd["bg"] = "green"
      self.test0207Cmd["activebackground"] = "green"
    else:
      self.test0207Cmd["bg"] = "red"
      self.test0207Cmd["activebackground"] = "red"
    if self.GT1000.LED_ROOF[1]:
      self.test0208Cmd["bg"] = "green"
      self.test0208Cmd["activebackground"] = "green"
    else:
      self.test0208Cmd["bg"] = "red"
      self.test0208Cmd["activebackground"] = "red"
    if self.GT1000.LED_ROOF[2]:
      self.test0209Cmd["bg"] = "green"
      self.test0209Cmd["activebackground"] = "green"
    else:
      self.test0209Cmd["bg"] = "red"
      self.test0209Cmd["activebackground"] = "red"





  def test0201Cmd__click(self):
    print("test0201")
  def test0202Cmd__click(self):
    print("test0202")
  def test0203Cmd__click(self):
    print("test0203")
  def test0204Cmd__click(self):
    print("test0204")
  def test0205Cmd__click(self):
    print("test0205")
  def test0206Cmd__click(self):
    print("test0206")
  def test0207Cmd__click(self):
    print("test0207")
  def test0208Cmd__click(self):
    print("test0208")
  def test0209Cmd__click(self):
    print("test0209")

  # Test 3
  def test03Cmd__click(self):
    print("test03")
    self.GT1000.clear_outputs()
    tChip = 0x39
    tPin = 0x10
    rPin = 2

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.PWR_FLIP[2]:
      self.test0301Cmd["bg"] = "green"
      self.test0301Cmd["activebackground"] = "green"
    else:
      self.test0301Cmd["bg"] = "red"
      self.test0301Cmd["activebackground"] = "red"
    #exit()
  def test0301Cmd__click(self):
    print("test0301")

  # Test 4
  def test04Cmd__click(self):
    print("test04")
    self.GT1000.clear_outputs()
    tChip = 0x39
    tPin = 0x80
    rPin = 0

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.AFB1[15]:
      self.test0401Cmd["bg"] = "green"
      self.test0401Cmd["activebackground"] = "green"
    else:
      self.test0401Cmd["bg"] = "red"
      self.test0401Cmd["activebackground"] = "red"
    if self.GT1000.GND[1]:
      self.test0402Cmd["bg"] = "green"
      self.test0402Cmd["activebackground"] = "green"
    else:
      self.test0402Cmd["bg"] = "red"
      self.test0402Cmd["activebackground"] = "red"
    if self.GT1000.GND[2]:
      self.test0403Cmd["bg"] = "green"
      self.test0403Cmd["activebackground"] = "green"
    else:
      self.test0403Cmd["bg"] = "red"
      self.test0403Cmd["activebackground"] = "red"
    if self.GT1000.WASHER[1]:
      self.test0404Cmd["bg"] = "green"
      self.test0404Cmd["activebackground"] = "green"
    else:
      self.test0404Cmd["bg"] = "red"
      self.test0404Cmd["activebackground"] = "red"
    if self.GT1000.AFB1[18]:
      self.test0405Cmd["bg"] = "green"
      self.test0405Cmd["activebackground"] = "green"
    else:
      self.test0405Cmd["bg"] = "red"
      self.test0405Cmd["activebackground"] = "red"
    if self.GT1000.AFB1[6]:
      self.test0406Cmd["bg"] = "green"
      self.test0406Cmd["activebackground"] = "green"
    else:
      self.test0406Cmd["bg"] = "red"
      self.test0406Cmd["activebackground"] = "red"




    #exit()
  def test0401Cmd__click(self):
    print("test0401")
  def test0402Cmd__click(self):
    print("test0402")
  def test0403Cmd__click(self):
    print("test0403")
  def test0404Cmd__click(self):
    print("test0404")
  def test0405Cmd__click(self):
    print("test0405")
  def test0406Cmd__click(self):
    print("test0406")

  # Test 5
  def test05Cmd__click(self):
    print("test05")
    self.GT1000.clear_outputs()
    tChip = 0x39
    tPin = 0x20
    rPin = 0x01

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.PWR_FLIP[1]:
      self.test0501Cmd["bg"] = "green"
      self.test0501Cmd["activebackground"] = "green"
    else:
      self.test0501Cmd["bg"] = "red"
      self.test0501Cmd["activebackground"] = "red"
    #exit()
  def test0501Cmd__click(self):
    print("test0501")

  # Test 6
  def test06Cmd__click(self):
    print("test06")
    self.GT1000.clear_outputs()
    tChip = 0x39
    tPin = 0x40
    rPin = 0x01

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.LED_ROOF[3]:
      self.test0601Cmd["bg"] = "green"
      self.test0601Cmd["activebackground"] = "green"
    else:
      self.test0601Cmd["bg"] = "red"
      self.test0601Cmd["activebackground"] = "red"
    if self.GT1000.AFB1[22]:
      self.test0602Cmd["bg"] = "green"
      self.test0602Cmd["activebackground"] = "green"
    else:
      self.test0602Cmd["bg"] = "red"
      self.test0602Cmd["activebackground"] = "red"
    #exit()
  def test0601Cmd__click(self):
    print("test0601")
  def test0602Cmd__click(self):
    print("test0602")

  # Test 7
  def test07Cmd__click(self):
    print("test07")
    self.GT1000.clear_outputs()
    tChip = 0x39
    tPin = 0x01
    rPin = 0x01

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.LED_ROOF[6]:
      self.test0701Cmd["bg"] = "green"
      self.test0701Cmd["activebackground"] = "green"
    else:
      self.test0701Cmd["bg"] = "red"
      self.test0701Cmd["activebackground"] = "red"
    #exit()
  def test0701Cmd__click(self):
    print("test0701")

  # Test 8
  def test08Cmd__click(self):
    print("test08")
    self.GT1000.clear_outputs()
    tChip = 0x39
    tPin = 0x02
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.LED_BUMPER[3]:
      self.test0801Cmd["bg"] = "green"
      self.test0801Cmd["activebackground"] = "green"
    else:
      self.test0801Cmd["bg"] = "red"
      self.test0801Cmd["activebackground"] = "red"
    if self.GT1000.AFB1[10]:
      self.test0802Cmd["bg"] = "green"
      self.test0802Cmd["activebackground"] = "green"
    else:
      self.test0802Cmd["bg"] = "red"
      self.test0802Cmd["activebackground"] = "red"
    #exit()
  def test0801Cmd__click(self):
    print("test0801")
  def test0802Cmd__click(self):
    print("test0802")

  # Test 9
  def test09Cmd__click(self):
    print("test09")
    self.GT1000.clear_outputs()
    tChip = 0x38
    tPin = 0x04
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.LED_BUMPER[6]:
      self.test0901Cmd["bg"] = "green"
      self.test0901Cmd["activebackground"] = "green"
    else:
      self.test0901Cmd["bg"] = "red"
      self.test0901Cmd["activebackground"] = "red"
    #exit()
  def test0901Cmd__click(self):
    print("test0901")

  # Test 10
  def test10Cmd__click(self):
    print("test10")
    self.GT1000.clear_outputs()
    tChip = 0x38
    tPin = 0x08
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.LED_HOOD[2]:
      self.test1001Cmd["bg"] = "green"
      self.test1001Cmd["activebackground"] = "green"
    else:
      self.test1001Cmd["bg"] = "red"
      self.test1001Cmd["activebackground"] = "red"
    #exit()
  def test1001Cmd__click(self):
    print("test1001")

  # Test 11
  def test11Cmd__click(self):
    print("test11")
    self.GT1000.clear_outputs()
    tChip = 0x38
    tPin = 0x10
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.DLC1[6]:
      self.test1101Cmd["bg"] = "green"
      self.test1101Cmd["activebackground"] = "green"
    else:
      self.test1101Cmd["bg"] = "red"
      self.test1101Cmd["activebackground"] = "red"
    if self.GT1000.DLC2[6]:
      self.test1102Cmd["bg"] = "green"
      self.test1102Cmd["activebackground"] = "green"
    else:
      self.test1102Cmd["bg"] = "red"
      self.test1102Cmd["activebackground"] = "red"
    if self.GT1000.KEY_PAD[6]:
      self.test1103Cmd["bg"] = "green"
      self.test1103Cmd["activebackground"] = "green"
    else:
      self.test1103Cmd["bg"] = "red"
      self.test1103Cmd["activebackground"] = "red"
    #exit(
  def test1101Cmd__click(self):
    print("test1101")
  def test1102Cmd__click(self):
    print("test1102")
  def test1103Cmd__click(self):
    print("test1103")

  # Test 12
  def test12Cmd__click(self):
    print("test12")
    self.GT1000.clear_outputs()
    tChip = 0x38
    tPin = 0x80
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.SNS[1]:
      self.test1201Cmd["bg"] = "green"
      self.test1201Cmd["activebackground"] = "green"
    else:
      self.test1201Cmd["bg"] = "red"
      self.test1201Cmd["activebackground"] = "red"
    #exit()
  def test1201Cmd__click(self):
    print("test1201")

  # Test 13
  def test13Cmd__click(self):
    print("test13")
    self.GT1000.clear_outputs()
    tChip = 0x38
    tPin = 0x20
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.SNS[2]:
      self.test1301Cmd["bg"] = "green"
      self.test1301Cmd["activebackground"] = "green"
    else:
      self.test1301Cmd["bg"] = "red"
      self.test1301Cmd["activebackground"] = "red"
    #exit()
  def test1301Cmd__click(self):
    print("test1301")

  # Test 14
  def test14Cmd__click(self):
    print("test14")
    self.GT1000.clear_outputs()
    tChip = 0x38
    tPin = 0x40
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.DLC1[1]:
      self.test1401Cmd["bg"] = "green"
      self.test1401Cmd["activebackground"] = "green"
    else:
      self.test1401Cmd["bg"] = "red"
      self.test1401Cmd["activebackground"] = "red"
    if self.GT1000.DLC2[1]:
      self.test1402Cmd["bg"] = "green"
      self.test1402Cmd["activebackground"] = "green"
    else:
      self.test1402Cmd["bg"] = "red"
      self.test1402Cmd["activebackground"] = "red"
    if self.GT1000.KEY_PAD[2]:
      self.test1403Cmd["bg"] = "green"
      self.test1403Cmd["activebackground"] = "green"
    else:
      self.test1403Cmd["bg"] = "red"
      self.test1403Cmd["activebackground"] = "red"
    #exit()
  def test1401Cmd__click(self):
    print("test1401")
  def test1402Cmd__click(self):
    print("test1402")
  def test1403Cmd__click(self):
    print("test1403")

  # Test 15
  def test15Cmd__click(self):
    print("test15")
    self.GT1000.clear_outputs()
    tChip = 0x38
    tPin = 0x01
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.DLC1[2]:
      self.test1501Cmd["bg"] = "green"
      self.test1501Cmd["activebackground"] = "green"
    else:
      self.test1501Cmd["bg"] = "red"
      self.test1501Cmd["activebackground"] = "red"
    if self.GT1000.DLC2[2]:
      self.test1502Cmd["bg"] = "green"
      self.test1502Cmd["activebackground"] = "green"
    else:
      self.test1502Cmd["bg"] = "red"
      self.test1502Cmd["activebackground"] = "red"
    if self.GT1000.KEY_PAD[5]:
      self.test1503Cmd["bg"] = "green"
      self.test1503Cmd["activebackground"] = "green"
    else:
      self.test1503Cmd["bg"] = "red"
      self.test1503Cmd["activebackground"] = "red"

    #exit()
  def test1501Cmd__click(self):
    print("test1501")
  def test1502Cmd__click(self):
    print("test1502")
  def test1503Cmd__click(self):
    print("test1503")

  # Test 16
  def test16Cmd__click(self):
    print("test16")
    self.GT1000.clear_outputs()
    tChip = 0x3A
    tPin = 0x10
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.LED_HOOD[4]:
      self.test1601Cmd["bg"] = "green"
      self.test1601Cmd["activebackground"] = "green"
    else:
      self.test1601Cmd["bg"] = "red"
      self.test1601Cmd["activebackground"] = "red"
    #exit()
  def test1601Cmd__click(self):
    print("test1601")

  # Test 17
  def test17Cmd__click(self):
    print("test17")
    self.GT1000.clear_outputs()
    tChip = 0x3A
    tPin = 0x80
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.SW_1[3]:
      self.test1701Cmd["bg"] = "green"
      self.test1701Cmd["activebackground"] = "green"
    else:
      self.test1701Cmd["bg"] = "red"
      self.test1701Cmd["activebackground"] = "red"
    #exit()
  def test1701Cmd__click(self):
    print("test1701")

  # Test 18
  def test18Cmd__click(self):
    print("test18")
    self.GT1000.clear_outputs()
    tChip = 0x3A
    tPin = 0x20
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.SW_1[1]:
      self.test1801Cmd["bg"] = "green"
      self.test1801Cmd["activebackground"] = "green"
    else:
      self.test1801Cmd["bg"] = "red"
      self.test1801Cmd["activebackground"] = "red"
    #exit()
  def test1801Cmd__click(self):
    print("test1801")

  # Test 19
  def test19Cmd__click(self):
    print("test19")
    self.GT1000.clear_outputs()
    tChip = 0x3A
    tPin = 0x40
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.LED_L[3]:
      self.test1901Cmd["bg"] = "green"
      self.test1901Cmd["activebackground"] = "green"
    else:
      self.test1901Cmd["bg"] = "red"
      self.test1901Cmd["activebackground"] = "red"
    #exit()
  def test1901Cmd__click(self):
    print("test1901")

  # Test 20
  def test20Cmd__click(self):
    print("test20")
    self.GT1000.clear_outputs()
    tChip = 0x3A
    tPin = 0x01
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.LED_R[3]:
      self.test2001Cmd["bg"] = "green"
      self.test2001Cmd["activebackground"] = "green"
    else:
      self.test2001Cmd["bg"] = "red"
      self.test2001Cmd["activebackground"] = "red"
    #exit()
  def test2001Cmd__click(self):
    print("test2001")

  # Test 21
  def test21Cmd__click(self):
    print("test21")
    self.GT1000.clear_outputs()
    tChip = 0x3C
    tPin = 0x10
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.AFB1[19]:
      self.test2101Cmd["bg"] = "green"
      self.test2101Cmd["activebackground"] = "green"
    else:
      self.test2101Cmd["bg"] = "red"
      self.test2101Cmd["activebackground"] = "red"
    #exit()
  def test2101Cmd__click(self):
    print("test2101")

  # Test 22
  def test22Cmd__click(self):
    print("test22")
    self.GT1000.clear_outputs()
    tChip = 0x3C
    tPin = 0x20
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.WASHER[2]:
      self.test2201Cmd["bg"] = "green"
      self.test2201Cmd["activebackground"] = "green"
    else:
      self.test2201Cmd["bg"] = "red"
      self.test2201Cmd["activebackground"] = "red"
    #exit()
  def test2201Cmd__click(self):
    print("test2201")

  # Test 23
  def test23Cmd__click(self):
    print("test23")
    self.GT1000.clear_outputs()
    tChip = 0x3C
    tPin = 0x40
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.S1X[1]:
      self.test2301Cmd["bg"] = "green"
      self.test2301Cmd["activebackground"] = "green"
    else:
      self.test2301Cmd["bg"] = "red"
      self.test2301Cmd["activebackground"] = "red"
    #exit()
  def test2301Cmd__click(self):
    print("test2301")

  # Test 24
  def test24Cmd__click(self):
    print("test24")
    self.GT1000.clear_outputs()
    tChip = 0x3C
    tPin = 0x80
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.S1X[2]:
      self.test2401Cmd["bg"] = "green"
      self.test2401Cmd["activebackground"] = "green"
    else:
      self.test2401Cmd["bg"] = "red"
      self.test2401Cmd["activebackground"] = "red"
    #exit()
  def test2401Cmd__click(self):
    print("test2401")

  # Test 25
  def test25Cmd__click(self):
    print("test25")
    self.GT1000.clear_outputs()
    tChip = 0x3B
    tPin = 0x80
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.AFB1[4]:
      self.test2501Cmd["bg"] = "green"
      self.test2501Cmd["activebackground"] = "green"
    else:
      self.test2501Cmd["bg"] = "red"
      self.test2501Cmd["activebackground"] = "red"
    if self.GT1000.AFB1[29]:
      self.test2502Cmd["bg"] = "green"
      self.test2502Cmd["activebackground"] = "green"
    else:
      self.test2502Cmd["bg"] = "red"
      self.test2502Cmd["activebackground"] = "red"
    #exit()
  def test2501Cmd__click(self):
    print("test2501")
  def test2502Cmd__click(self):
    print("test2502")

  # Test 26
  def test26Cmd__click(self):
    print("test26")
    self.GT1000.clear_outputs()
    tChip = 0x3B
    tPin = 0x40
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.LED_BUMPER[4]:
      self.test2601Cmd["bg"] = "green"
      self.test2601Cmd["activebackground"] = "green"
    else:
      self.test2601Cmd["bg"] = "red"
      self.test2601Cmd["activebackground"] = "red"
    #exit()
  def test2601Cmd__click(self):
    print("test2601")

  # Test 27
  def test27Cmd__click(self):
    print("test27")
    self.GT1000.clear_outputs()
    tChip = 0x3B
    tPin = 0x20
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.AFB1[31]:
      self.test2701Cmd["bg"] = "green"
      self.test2701Cmd["activebackground"] = "green"
    else:
      self.test2701Cmd["bg"] = "red"
      self.test2701Cmd["activebackground"] = "red"
    if self.GT1000.WIPER[4]:
      self.test2702Cmd["bg"] = "green"
      self.test2702Cmd["activebackground"] = "green"
    else:
      self.test2702Cmd["bg"] = "red"
      self.test2702Cmd["activebackground"] = "red"
    #exit()
  def test2701Cmd__click(self):
    print("test2701")
  def test2702Cmd__click(self):
    print("test2702")
  def test2703Cmd__click(self):
    print("test2703")

  # Test 28
  def test28Cmd__click(self):
    print("test28")
    self.GT1000.clear_outputs()
    tChip = 0x3B
    tPin = 0x10
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.WIPER[2]:
      self.test2801Cmd["bg"] = "green"
      self.test2801Cmd["activebackground"] = "green"
    else:
      self.test2801Cmd["bg"] = "red"
      self.test2801Cmd["activebackground"] = "red"
    #exit()
  def test2801Cmd__click(self):
    print("test2801")
  def test2802Cmd__click(self):
    print("test2802")

  # Test 29
  def test29Cmd__click(self):
    print("test29")
    self.GT1000.clear_outputs()
    tChip = 0x3B
    tPin = 0x08
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.AFB1[23]:
      self.test2901Cmd["bg"] = "green"
      self.test2901Cmd["activebackground"] = "green"
    else:
      self.test2901Cmd["bg"] = "red"
      self.test2901Cmd["activebackground"] = "red"
    if self.GT1000.AFB1[35]:
      self.test2902Cmd["bg"] = "green"
      self.test2902Cmd["activebackground"] = "green"
    else:
      self.test2902Cmd["bg"] = "red"
      self.test2902Cmd["activebackground"] = "red"
    #exit()
  def test2901Cmd__click(self):
    print("test2901")
  def test2902Cmd__click(self):
    print("test2902")

  # Test 30
  def test30Cmd__click(self):
    print("test30")
    self.GT1000.clear_outputs()
    tChip = 0x3B
    tPin = 0x04
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.WIPER[3]:
      self.test3001Cmd["bg"] = "green"
      self.test3001Cmd["activebackground"] = "green"
    else:
      self.test3001Cmd["bg"] = "red"
      self.test3001Cmd["activebackground"] = "red"
    #exit()
  def test3001Cmd__click(self):
    print("test3001")

  # Test 31
  def test31Cmd__click(self):
    print("test31")
    self.GT1000.clear_outputs()
    tChip = 0x3B
    tPin = 0x02
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.LED_ROOF[4]:
      self.test3101Cmd["bg"] = "green"
      self.test3101Cmd["activebackground"] = "green"
    else:
      self.test3101Cmd["bg"] = "red"
      self.test3101Cmd["activebackground"] = "red"
    if self.GT1000.LED_ROOF[5]:
      self.test3102Cmd["bg"] = "green"
      self.test3102Cmd["activebackground"] = "green"
    else:
      self.test3102Cmd["bg"] = "red"
      self.test3102Cmd["activebackground"] = "red"
    #exit()
  def test3101Cmd__click(self):
    print("test3101")
  def test3102Cmd__click(self):
    print("test3102")

  # Test 32
  def test32Cmd__click(self):
    print("test32")
    self.GT1000.clear_outputs()
    tChip = 0x3B
    tPin = 0x01
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.LED_L[2]:
      self.test3201Cmd["bg"] = "green"
      self.test3201Cmd["activebackground"] = "green"
    else:
      self.test3201Cmd["bg"] = "red"
      self.test3201Cmd["activebackground"] = "red"
    if self.GT1000.LED_R[2]:
      self.test3202Cmd["bg"] = "green"
      self.test3202Cmd["activebackground"] = "green"
    else:
      self.test3202Cmd["bg"] = "red"
      self.test3202Cmd["activebackground"] = "red"
    if self.GT1000.LED_HOOD[3]:
      self.test3203Cmd["bg"] = "green"
      self.test3203Cmd["activebackground"] = "green"
    else:
      self.test3203Cmd["bg"] = "red"
      self.test3203Cmd["activebackground"] = "red"

    #exit()
  def test3201Cmd__click(self):
    print("test3201")
  def test3202Cmd__click(self):
    print("test3202")
  def test3203Cmd__click(self):
    print("test3203")

  # Test 33
  def test33Cmd__click(self):
    print("test33")
    self.GT1000.clear_outputs()
    tChip = 0x3D
    tPin = 0x04
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.DLC2[3]:
      self.test3301Cmd["bg"] = "green"
      self.test3301Cmd["activebackground"] = "green"
    else:
      self.test3301Cmd["bg"] = "red"
      self.test3301Cmd["activebackground"] = "red"
    if self.GT1000.KEY_PAD[1]:
      self.test3302Cmd["bg"] = "green"
      self.test3302Cmd["activebackground"] = "green"
    else:
      self.test3302Cmd["bg"] = "red"
      self.test3302Cmd["activebackground"] = "red"
    #exit()
  def test3301Cmd__click(self):
    print("test3301")
  def test3302Cmd__click(self):
    print("test3302")

  # Test 34
  def test34Cmd__click(self):
    print("test34")
    self.GT1000.clear_outputs()
    tChip = 0x3D
    tPin = 0x08
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.DLC2[4]:
      self.test3401Cmd["bg"] = "green"
      self.test3401Cmd["activebackground"] = "green"
    else:
      self.test3401Cmd["bg"] = "red"
      self.test3401Cmd["activebackground"] = "red"
    #exit()
  def test3401Cmd__click(self):
    print("test3401")

  # Test 35
  def test35Cmd__click(self):
    print("test35")
    self.GT1000.clear_outputs()
    tChip = 0x3D
    tPin = 0x10
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.DLC2[5]:
      self.test3501Cmd["bg"] = "green"
      self.test3501Cmd["activebackground"] = "green"
    else:
      self.test3501Cmd["bg"] = "red"
      self.test3501Cmd["activebackground"] = "red"
    #exit()
  def test3501Cmd__click(self):
    print("test3501")

  # Test 36
  def test36Cmd__click(self):
    print("test36")
    self.GT1000.clear_outputs()
    tChip = 0x3D
    tPin = 0x02
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.AFB1[28]:
      self.test3601Cmd["bg"] = "green"
      self.test3601Cmd["activebackground"] = "green"
    else:
      self.test3601Cmd["bg"] = "red"
      self.test3601Cmd["activebackground"] = "red"
    if self.GT1000.AFB1[32]:
      self.test3602Cmd["bg"] = "green"
      self.test3602Cmd["activebackground"] = "green"
    else:
      self.test3602Cmd["bg"] = "red"
      self.test3602Cmd["activebackground"] = "red"
    if self.GT1000.AFB1[26]:
      self.test3603Cmd["bg"] = "green"
      self.test3603Cmd["activebackground"] = "green"
    else:
      self.test3603Cmd["bg"] = "red"
      self.test3603Cmd["activebackground"] = "red"
    if self.GT1000.AFB1[30]:
      self.test3604Cmd["bg"] = "green"
      self.test3604Cmd["activebackground"] = "green"
    else:
      self.test3604Cmd["bg"] = "red"
      self.test3604Cmd["activebackground"] = "red"
    if self.GT1000.AFB1[36]:
      self.test3605Cmd["bg"] = "green"
      self.test3605Cmd["activebackground"] = "green"
    else:
      self.test3605Cmd["bg"] = "red"
      self.test3605Cmd["activebackground"] = "red"



    #exit()
  def test3601Cmd__click(self):
    print("test3601")
  def test3602Cmd__click(self):
    print("test3602")
  def test3603Cmd__click(self):
    print("test3603")
  def test3604Cmd__click(self):
    print("test3604")
  def test3605Cmd__click(self):
    print("test3605")


  # Test 37
  def test37Cmd__click(self):
    print("test37")
    self.GT1000.clear_outputs()
    tChip = 0x3D
    tPin = 0x01
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(30/1000)
    self.GT1000.write_output(tChip,tPin)
    time.sleep(30/1000)
    if self.GT1000.SW_1[2]:
      self.test3701Cmd["bg"] = "green"
      self.test3701Cmd["activebackground"] = "green"
    else:
      self.test3701Cmd["bg"] = "red"
      self.test3701Cmd["activebackground"] = "red"
    if self.GT1000.SW_1[8]:
      self.test3702Cmd["bg"] = "green"
      self.test3702Cmd["activebackground"] = "green"
    else:
      self.test3702Cmd["bg"] = "red"
      self.test3702Cmd["activebackground"] = "red"
    #exit()
  def test3701Cmd__click(self):
    print("test3701")
  def test3702Cmd__click(self):
    print("test3702")


  def station01Cmd__click(self):
    return
    print("1")
    s = self.station01Text.get()
    if self.station01Text.get() == "":
      self.station01Cmd["bg"] = "green"
      self.station01Cmd["activebackground"] = "green"
      return
    self.GT1000.enableStations([8])
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
          self.station01Cmd["activebackground"] = "red"
          self.station01Text.set(s + "\nTest Aborted")
          return
        if self.GT1000.GT_Fail:
          print("{Test FAILED}")
          self.station01Cmd["bg"] = "red"
          self.station01Cmd["activebackground"] = "red"
          self.station01Text.set(s + "\nTest FAILED")
          return
        if self.GT1000.GT_Pass:
          print("{Test PASSED}")
          self.station01Cmd["bg"] = "green"
          self.station01Cmd["activebackground"] = "green"
          self.station01Text.set(s +"\n << PASSED >>")
          return
      self.station01Cmd["bg"] = "red"
      self.station01Cmd["activebackground"] = "red"
      self.station01Text.set(s + "\nAbnormal Completion")
  def station02Cmd__click(self):
    print("2")
    s = self.station02Text.get()
    if self.station02Text.get() == "":
      self.station02Cmd["bg"] = "green"
      self.station02Cmd["activebackground"] = "green"
      return
    if self.testPart == "4568":
      self.GT1000.enableStations([7])
    else:
      self.GT1000.enableStations([6])
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
          self.station02Cmd["activebackground"] = "red"
          self.station02Text.set(s + "\nTest Aborted")
          return
        if self.GT1000.GT_Fail:
          print("{Test FAILED}")
          self.station02Cmd["bg"] = "red"
          self.station02Cmd["activebackground"] = "red"
          self.station02Text.set(s + "\nTest FAILED")
          return
        if self.GT1000.GT_Pass:
          print("{Test PASSED}")
          self.station02Cmd["bg"] = "green"
          self.station02Cmd["activebackground"] = "green"
          self.station02Text.set(s +"\n << PASSED >>")
          return
      self.station02Cmd["bg"] = "red"
      self.station02Cmd["activebackground"] = "red"
      self.station02Text.set(s + "\nAbnormal Completion")
  def station03Cmd__click(self):
    print("3")
    s = self.station03Text.get()
    if self.station03Text.get() == "":
      self.station03Cmd["bg"] = "green"
      self.station03Cmd["activebackground"] = "green"
      return
    self.GT1000.enableStations([5])
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
          self.station03Cmd["activebackground"] = "red"
          self.station03Text.set(s + "\nTest Aborted")
          return
        if self.GT1000.GT_Fail:
          print("{Test FAILED}")
          self.station03Cmd["bg"] = "red"
          self.station03Cmd["activebackground"] = "red"
          self.station03Text.set(s + "\nTest FAILED")
          return
        if self.GT1000.GT_Pass:
          print("{Test PASSED}")
          self.station03Cmd["bg"] = "green"
          self.station03Cmd["activebackground"] = "green"
          self.station03Text.set(s +"\n << PASSED >>")
          return
      self.station03Cmd["bg"] = "red"
      self.station03Cmd["activebackground"] = "red"
      self.station03Text.set(s + "\nAbnormal Completion")
  def station04Cmd__click(self):
    print("4")
    if self.station04Text.get() == "":
      self.station04Cmd["bg"] = "green"
      self.station04Cmd["activebackground"] = "green"
      return
    s = self.station04Text.get()
    self.GT1000.enableStations([4])
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
          self.station04Cmd["activebackground"] = "red"
          self.station04Text.set(s + "\nTest Aborted")
          return
        if self.GT1000.GT_Fail:
          print("{Test FAILED}")
          self.station04Cmd["bg"] = "red"
          self.station04Cmd["activebackground"] = "red"
          self.station04Text.set(s + "\nTest FAILED")
          return
        if self.GT1000.GT_Pass:
          print("{Test PASSED}")
          self.station04Cmd["bg"] = "green"
          self.station04Cmd["activebackground"] = "green"
          self.station04Text.set(s +"\n << PASSED >>")
          return
      self.station04Cmd["bg"] = "red"
      self.station04Cmd["activebackground"] = self.station04Cmd["bg"]
      self.station04Text.set(s + "\nAbnormal Completion")
  def station05Cmd__click(self):
    print("5")
    if self.station05Text.get() == "":
      self.station05Cmd["bg"] = "green"
      self.station05Cmd["activebackground"] = "green"
      return
    s = self.station05Text.get()
    self.GT1000.enableStations([3])
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
          self.station05Cmd["activebackground"] = "red"
          self.station05Text.set(s + "\nTest Aborted")
          return
        if self.GT1000.GT_Fail:
          print("{Test FAILED}")
          self.station05Cmd["bg"] = "red"
          self.station05Cmd["activebackground"] = "red"
          self.station05Text.set(s + "\nTest FAILED")
          return
        if self.GT1000.GT_Pass:
          print("{Test PASSED}")
          self.station05Cmd["bg"] = "green"
          self.station05Cmd["activebackground"] = "green"
          self.station05Text.set(s +"\n << PASSED >>")
          return
      self.station05Cmd["bg"] = "red"
      self.station05Cmd["activebackground"] = "red"
      self.station05Text.set(s + "\nAbnormal Completion")
  def station06Cmd__click(self):
    print("6")
    if self.station06Text.get() == "":
      self.station06Cmd["bg"] = "green"
      self.station06Cmd["activebackground"] = "green"
      return
    s = self.station06Text.get()
    self.GT1000.enableStations([2])
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
          self.station06Cmd["activebackground"] = "red"
          self.station06Text.set(s + "\nTest Aborted")
          return
        if self.GT1000.GT_Fail:
          print("{Test FAILED}")
          self.station06Cmd["bg"] = "red"
          self.station06Cmd["activebackground"] = "red"
          self.station06Text.set(s + "\nTest FAILED")
          return
        if self.GT1000.GT_Pass:
          print("{Test PASSED}")
          self.station06Cmd["bg"] = "green"
          self.station06Cmd["activebackground"] = "green"
          self.station06Text.set(s +"\n << PASSED >>")
          return
      self.station06Cmd["bg"] = "red"
      self.station06Cmd["activebackground"] = "red"
      self.station06Text.set(s + "\nAbnormal Completion")
  def station07Cmd__click(self):
    print("7")
    if self.station07Text.get() == "":
      self.station07Cmd["bg"] = "green"
      self.station07Cmd["activebackground"] = "green"
      return
    s = self.station07Text.get()
    self.GT1000.enableStations([1])
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
          self.station07Cmd["activebackground"] = "red"
          self.station07Text.set(s + "\nTest Aborted")
          return
        if self.GT1000.GT_Fail:
          print("{Test FAILED}")
          self.station07Cmd["bg"] = "red"
          self.station07Cmd["activebackground"] = "red"
          self.station07Text.set(s + "\nTest FAILED")
          return
        if self.GT1000.GT_Pass:
          print("{Test PASSED}")
          self.station07Cmd["bg"] = "green"
          self.station07Cmd["activebackground"] = "green"
          self.station07Text.set(s +"\n << PASSED >>")
          return
      self.station07Cmd["bg"] = "red"
      self.station07Cmd["activebackground"] = "red"
      self.station07Text.set(s + "\nAbnormal Completion")
  def station08Cmd__click(self):
    print("8")
    if self.station08Text.get() == "":
      self.station08Cmd["bg"] = "green"
      self.station08Cmd["activebackground"] = "green"
      return
    if self.testPart == "4568":
      self.GT1000.enableStations([10])
    else:
      self.GT1000.enableStations([9])
    s = self.station08Text.get()
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
          self.station08Cmd["activebackground"] = "red"
          self.station08Text.set(s + "\nTest Aborted")
          return
        if self.GT1000.GT_Fail:
          print("{Test FAILED}")
          self.station08Cmd["bg"] = "red"
          self.station08Cmd["activebackground"] = "red"
          self.station08Text.set(s + "\nTest FAILED")
          return
        if self.GT1000.GT_Pass:
          print("{Test PASSED}")
          self.station08Cmd["bg"] = "green"
          self.station08Cmd["activebackground"] = "green"
          self.station08Text.set(s +"\n << PASSED >>")
          return
      self.station08Cmd["bg"] = "red"
      self.station08Cmd["activebackground"] = "red"
      self.station08Text.set(s + "\nAbnormal Completion")
  def station09Cmd__click(self):
    print("9")
    if self.station09Text.get() == "":
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
          self.station09Cmd["activebackground"] = "red"
          self.station09Text.set(s + "\nTest Aborted")
          return
        if self.GT1000.GT_Fail:
          print("{Test FAILED}")
          self.station09Cmd["bg"] = "red"
          self.station09Cmd["activebackground"] = "red"
          self.station09Text.set(s + "\nTest FAILED")
          return
        if self.GT1000.GT_Pass:
          print("{Test PASSED}")
          self.station09Cmd["bg"] = "green"
          self.station09Cmd["activebackground"] = "green"
          self.station09Text.set(s +"\n << PASSED >>")
          return
      self.station09Cmd["bg"] = "red"
      self.station09Cmd["activebackground"] = "red"
      self.station09Text.set(s + "\nAbnormal Completion")
  def station10Cmd__click(self):
    print("10")
    if self.station10Text.get() == "":
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
          self.station10Cmd["activebackground"] = "red"
          self.station10Text.set(s + "\nTest Aborted")
          return
        if self.GT1000.GT_Fail:
          print("{Test FAILED}")
          self.station10Cmd["bg"] = "red"
          self.station10Cmd["activebackground"] = "red"
          self.station10Text.set(s + "\nTest FAILED")
          return
        if self.GT1000.GT_Pass:
          print("{Test PASSED}")
          self.station10Cmd["bg"] = "green"
          self.station10Cmd["activebackground"] = "green"
          self.station10Text.set(s +"\n << PASSED >>")
          return
      self.station10Cmd["bg"] = "red"
      self.station10Cmd["activebackground"] = "red"
      self.station10Text.set(s + "\nAbnormal Completion")
  def station11Cmd__click(self):
    print("11")
    if self.station11Text.get() == "":
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
          self.station11Cmd["activebackground"] = "red"
          self.station11Text.set(s + "\nTest Aborted")
          return
        if self.GT1000.GT_Fail:
          print("{Test FAILED}")
          self.station11Cmd["bg"] = "red"
          self.station11Cmd["activebackground"] = "red"
          self.station11Text.set(s + "\nTest FAILED")
          return
        if self.GT1000.GT_Pass:
          print("{Test PASSED}")
          self.station11Cmd["bg"] = "green"
          self.station11Cmd["activebackground"] = "green"
          self.station11Text.set(s +"\n << PASSED >>")
          return
      self.station11Cmd["bg"] = "red"
      self.station11Cmd["activebackground"] = "red"
      self.station11Text.set(s + "\nAbnormal Completion")
  def station12Cmd__click(self):
    print("12")
    if self.station12Text.get() == "":
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
          self.station12Cmd["activebackground"] = "red"
          self.station12Text.set(s + "\nTest Aborted")
          return
        if self.GT1000.GT_Fail:
          print("{Test FAILED}")
          self.station12Cmd["bg"] = "red"
          self.station12Cmd["activebackground"] = "red"
          self.station12Text.set(s + "\nTest FAILED")
          return
        if self.GT1000.GT_Pass:
          print("{Test PASSED}")
          self.station12Cmd["bg"] = "green"
          self.station12Cmd["activebackground"] = "green"
          self.station12Text.set(s +"\n << PASSED >>")
          return
      self.station12Cmd["bg"] = "red"
      self.station12Cmd["activebackground"] = "red"
      self.station12Text.set(s + "\nAbnormal Completion")
  def station13Cmd__click(self):
    print("13")
    if self.station13Text.get() == "":
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
          self.station13Cmd["activebackground"] = "red"
          self.station13Text.set(s + "\nTest Aborted")
          return
        if self.GT1000.GT_Fail:
          print("{Test FAILED}")
          self.station13Cmd["bg"] = "red"
          self.station13Cmd["activebackground"] = "red"
          self.station13Text.set(s + "\nTest FAILED")
          return
        if self.GT1000.GT_Pass:
          print("{Test PASSED}")
          self.station13Cmd["bg"] = "green"
          self.station13Cmd["activebackground"] = "green"
          self.station13Text.set(s +"\n << PASSED >>")
          return
      self.station13Cmd["bg"] = "red"
      self.station13Cmd["activebackground"] = "red"
      self.station13Text.set(s + "\nAbnormal Completion")
  def station14Cmd__click(self):
    print("14")
    if self.station14Text.get() == "":
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
          self.station14Cmd["activebackground"] = "red"
          self.station14Text.set(s + "\nTest Aborted")
          return
        if self.GT1000.GT_Fail:
          print("{Test FAILED}")
          self.station14Cmd["bg"] = "red"
          self.station14Cmd["activebackground"] = "red"
          self.station14Text.set(s + "\nTest FAILED")
          return
        if self.GT1000.GT_Pass:
          print("{Test PASSED}")
          self.station14Cmd["bg"] = "green"
          self.station14Cmd["activebackground"] = "green"
          self.station14Text.set(s +"\n << PASSED >>")
          return
      self.station14Cmd["bg"] = "red"
      self.station14Cmd["activebackground"] = "red"
      self.station14Text.set(s + "\nAbnormal Completion")
  def station15Cmd__click(self):
    print("15")
# Old handling for non-entities
#    if self.station15Text.get() == "":
#      self.station15Cmd["bg"] = "green"
#      self.station15Cmd["activebackground"] = "green"
#      return
    self.GT1000.triggerCamera()
    time.sleep(0.5)
    self.update()
    self.checkForPass()


  def station16Cmd__click(self):
    print("<LOAD 4568>")
    self.testPart = "4568"
    self.resetButtonColours()
    self.station01Text.set("Press to Test\nLED_L")
    self.station02Text.set("Press to Test\nWIPER")
    self.station03Text.set("Press to Test\nSNS 1")
    self.station04Text.set("Press to Test\nAFB 1")
    self.station05Text.set("Press to Test\nACM 1")
    self.station06Text.set("Press to Test\nDLC 1")
    self.station07Text.set("Press to Test\nDLC 2")
    self.station08Text.set("Press to Test\nPWR_FLIP")
    self.station09Text.set("Press to Test\nWASHER")
    self.station10Text.set("Press to Test\nKEY_PAD")
    self.station11Text.set("Press to Test\nLED_R")
    self.station12Text.set("Press to Test\nLED_HOOD")
    self.station13Text.set("")
#    self.station13Text.set("Press to Test\nLED_ROOF")
    self.station14Text.set("Press to Test\nLED_BUMPER")
    self.station15Text.set("Camera")

  def station17Cmd__click(self):
    print("<LOAD 4569>")
    self.testPart = "4569"
    self.resetButtonColours()
    self.station01Text.set("Press to Test\nHELMET_FAN")
    self.station02Text.set("Press to Test\nAFB 2")
    self.station03Text.set("")
    self.station04Text.set("")
    self.station05Text.set("Press to Test\nACM 2")
    self.station06Text.set("")
    self.station07Text.set("Press to Test\nLED_CHASE_1")
    self.station08Text.set("Press to Test\nLED_CHASE_2")
    self.station09Text.set("")
    self.station10Text.set("Press to Test\nLED_CHASE_3")
    self.station11Text.set("Press to Test\nPARTICULE")
    self.station12Text.set("")
    self.station13Text.set("")
    self.station14Text.set("")
    self.station15Text.set("Camera")

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

    # Try exhausting all stations
    self.GT1000.enableStations([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])

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
       (self.station14Cmd["bg"] == "green") and \
       ((self.station15Cmd["bg"] == "green") or (self.testPart == "4569")):
      print("*** All Tests PASSED ***")
      self.GT1000.pulseRelease()
    if self.testPart == "4568":
      self.GT1000.enableStations([7])
    else:
      self.GT1000.enableStations([6])

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
    return
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
    self.station01Cmd["activebackground"]="grey90"
    self.station02Cmd["activebackground"]="grey90"
    self.station03Cmd["activebackground"]="grey90"
    self.station04Cmd["activebackground"]="grey90"
    self.station05Cmd["activebackground"]="grey90"
    self.station06Cmd["activebackground"]="grey90"
    self.station07Cmd["activebackground"]="grey90"
    self.station08Cmd["activebackground"]="grey90"
    self.station09Cmd["activebackground"]="grey90"
    self.station10Cmd["activebackground"]="grey90"
    self.station11Cmd["activebackground"]="grey90"
    self.station12Cmd["activebackground"]="grey90"
    self.station13Cmd["activebackground"]="grey90"
    self.station14Cmd["activebackground"]="grey90"
    self.station15Cmd["activebackground"]="grey90"
