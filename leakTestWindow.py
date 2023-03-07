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


    self.myScroll = Scrollbar(self)
    self.myScroll.grid(row=0,column=0)

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

    self.test00Text = StringVar()
    self.test0001Text = StringVar()
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
    gridHeight = 1
    rowIndex = 0
    fontHeight = 6


    self.test00Cmd = Button(self, textvariable=self.test00Text,command=self.test00Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test00Cmd.grid(row=0,column=7,sticky='w')
    self.test0001Cmd = Button(self, textvariable=self.test0001Text,command=self.test0001Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test0001Cmd.grid(row=1,column=7,sticky='w')

    # Test 1
    self.test01Cmd = Button(self, textvariable=self.test01Text,command=self.test01Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test01Cmd.grid(row=0,column=0,sticky='w')
    self.test0101Cmd = Button(self, textvariable=self.test0101Text,command=self.test0101Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test0101Cmd.grid(row=0,column=1,sticky='w')

    # Test 2
    rowIndex += 1
    self.test02Cmd = Button(self, textvariable=self.test02Text,command=self.test02Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test02Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test0201Cmd = Button(self, textvariable=self.test0201Text,command=self.test0201Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test0201Cmd.grid(row=rowIndex,column=1,sticky='w')
    self.test0202Cmd = Button(self, textvariable=self.test0202Text,command=self.test0202Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test0202Cmd.grid(row=rowIndex,column=2,sticky='w')
    self.test0203Cmd = Button(self, textvariable=self.test0203Text,command=self.test0203Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test0203Cmd.grid(row=rowIndex,column=3,sticky='w')
    self.test0204Cmd = Button(self, textvariable=self.test0204Text,command=self.test0204Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test0204Cmd.grid(row=rowIndex,column=4,sticky='w')
    self.test0205Cmd = Button(self, textvariable=self.test0205Text,command=self.test0205Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test0205Cmd.grid(row=rowIndex,column=5,sticky='w')
    rowIndex += 1
    self.test0206Cmd = Button(self, textvariable=self.test0206Text,command=self.test0206Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test0206Cmd.grid(row=rowIndex,column=1,sticky='w')
    self.test0207Cmd = Button(self, textvariable=self.test0207Text,command=self.test0207Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test0207Cmd.grid(row=rowIndex,column=2,sticky='w')
    self.test0208Cmd = Button(self, textvariable=self.test0208Text,command=self.test0208Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test0208Cmd.grid(row=rowIndex,column=3,sticky='w')
    self.test0209Cmd = Button(self, textvariable=self.test0209Text,command=self.test0209Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test0209Cmd.grid(row=rowIndex,column=4,sticky='w')

    # Test 3
    rowIndex += 1
    self.test03Cmd = Button(self, textvariable=self.test03Text,command=self.test03Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test03Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test0301Cmd = Button(self, textvariable=self.test0301Text,command=self.test0301Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test0301Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 4
    rowIndex += 1
    self.test04Cmd = Button(self, textvariable=self.test04Text,command=self.test04Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test04Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test0401Cmd = Button(self, textvariable=self.test0401Text,command=self.test0401Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test0401Cmd.grid(row=rowIndex,column=1,sticky='w')
    self.test0402Cmd = Button(self, textvariable=self.test0402Text,command=self.test0402Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test0402Cmd.grid(row=rowIndex,column=2,sticky='w')
    self.test0403Cmd = Button(self, textvariable=self.test0403Text,command=self.test0403Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test0403Cmd.grid(row=rowIndex,column=3,sticky='w')
    self.test0404Cmd = Button(self, textvariable=self.test0404Text,command=self.test0404Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test0404Cmd.grid(row=rowIndex,column=4,sticky='w')
    self.test0405Cmd = Button(self, textvariable=self.test0405Text,command=self.test0405Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test0405Cmd.grid(row=rowIndex,column=5,sticky='w')
    rowIndex += 1
    self.test0406Cmd = Button(self, textvariable=self.test0406Text,command=self.test0406Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test0406Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 5
    rowIndex += 1
    self.test05Cmd = Button(self, textvariable=self.test05Text,command=self.test05Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test05Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test0501Cmd = Button(self, textvariable=self.test0501Text,command=self.test0501Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test0501Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 6
    rowIndex += 1
    self.test06Cmd = Button(self, textvariable=self.test06Text,command=self.test06Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test06Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test0601Cmd = Button(self, textvariable=self.test0601Text,command=self.test0601Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test0601Cmd.grid(row=rowIndex,column=1,sticky='w')
    self.test0602Cmd = Button(self, textvariable=self.test0602Text,command=self.test0602Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test0602Cmd.grid(row=rowIndex,column=2,sticky='w')

    # Test 7
    rowIndex += 1
    self.test07Cmd = Button(self, textvariable=self.test07Text,command=self.test07Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test07Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test0701Cmd = Button(self, textvariable=self.test0701Text,command=self.test0701Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test0701Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 8
    rowIndex += 1
    self.test08Cmd = Button(self, textvariable=self.test08Text,command=self.test08Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test08Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test0801Cmd = Button(self, textvariable=self.test0801Text,command=self.test0801Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test0801Cmd.grid(row=rowIndex,column=1,sticky='w')
    self.test0802Cmd = Button(self, textvariable=self.test0802Text,command=self.test0802Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test0802Cmd.grid(row=rowIndex,column=2,sticky='w')

    # Test 9
    rowIndex += 1
    self.test09Cmd = Button(self, textvariable=self.test09Text,command=self.test09Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test09Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test0901Cmd = Button(self, textvariable=self.test0901Text,command=self.test0901Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test0901Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 10
    rowIndex += 1
    self.test10Cmd = Button(self, textvariable=self.test10Text,command=self.test10Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test10Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test1001Cmd = Button(self, textvariable=self.test1001Text,command=self.test1001Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test1001Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 11
    rowIndex += 1
    self.test11Cmd = Button(self, textvariable=self.test11Text,command=self.test11Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test11Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test1101Cmd = Button(self, textvariable=self.test1101Text,command=self.test1101Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test1101Cmd.grid(row=rowIndex,column=1,sticky='w')
    self.test1102Cmd = Button(self, textvariable=self.test1102Text,command=self.test1102Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test1102Cmd.grid(row=rowIndex,column=2,sticky='w')
    self.test1103Cmd = Button(self, textvariable=self.test1103Text,command=self.test1103Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test1103Cmd.grid(row=rowIndex,column=3,sticky='w')

    # Test 12
    rowIndex += 1
    self.test12Cmd = Button(self, textvariable=self.test12Text,command=self.test12Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test12Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test1201Cmd = Button(self, textvariable=self.test1201Text,command=self.test1201Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test1201Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 13
    rowIndex += 1
    self.test13Cmd = Button(self, textvariable=self.test13Text,command=self.test13Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test13Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test1301Cmd = Button(self, textvariable=self.test1301Text,command=self.test1301Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test1301Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 14
    rowIndex += 1
    self.test14Cmd = Button(self, textvariable=self.test14Text,command=self.test14Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test14Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test1401Cmd = Button(self, textvariable=self.test1401Text,command=self.test1401Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test1401Cmd.grid(row=rowIndex,column=1,sticky='w')
    self.test1402Cmd = Button(self, textvariable=self.test1402Text,command=self.test1402Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test1402Cmd.grid(row=rowIndex,column=2,sticky='w')
    self.test1403Cmd = Button(self, textvariable=self.test1403Text,command=self.test1403Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test1403Cmd.grid(row=rowIndex,column=3,sticky='w')

    # Test 15
    rowIndex += 1
    self.test15Cmd = Button(self, textvariable=self.test15Text,command=self.test15Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test15Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test1501Cmd = Button(self, textvariable=self.test1501Text,command=self.test1501Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test1501Cmd.grid(row=rowIndex,column=1,sticky='w')
    self.test1502Cmd = Button(self, textvariable=self.test1502Text,command=self.test1502Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test1502Cmd.grid(row=rowIndex,column=2,sticky='w')
    self.test1503Cmd = Button(self, textvariable=self.test1503Text,command=self.test1503Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test1503Cmd.grid(row=rowIndex,column=3,sticky='w')

    # Test 16
    rowIndex += 1
    self.test16Cmd = Button(self, textvariable=self.test16Text,command=self.test16Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test16Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test1601Cmd = Button(self, textvariable=self.test1601Text,command=self.test1601Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test1601Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 17
    rowIndex += 1
    self.test17Cmd = Button(self, textvariable=self.test17Text,command=self.test17Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test17Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test1701Cmd = Button(self, textvariable=self.test1701Text,command=self.test1701Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test1701Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 18
    rowIndex += 1
    self.test18Cmd = Button(self, textvariable=self.test18Text,command=self.test18Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test18Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test1801Cmd = Button(self, textvariable=self.test1801Text,command=self.test1801Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test1801Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 19
    rowIndex += 1
    self.test19Cmd = Button(self, textvariable=self.test19Text,command=self.test19Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test19Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test1901Cmd = Button(self, textvariable=self.test1901Text,command=self.test1901Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test1901Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 20
    rowIndex += 1
    self.test20Cmd = Button(self, textvariable=self.test20Text,command=self.test20Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test20Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test2001Cmd = Button(self, textvariable=self.test2001Text,command=self.test2001Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test2001Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 21
    rowIndex += 1
    self.test21Cmd = Button(self, textvariable=self.test21Text,command=self.test21Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test21Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test2101Cmd = Button(self, textvariable=self.test2101Text,command=self.test2101Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test2101Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 22
    rowIndex += 1
    self.test22Cmd = Button(self, textvariable=self.test22Text,command=self.test22Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test22Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test2201Cmd = Button(self, textvariable=self.test2201Text,command=self.test2201Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test2201Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 23
    rowIndex += 1
    self.test23Cmd = Button(self, textvariable=self.test23Text,command=self.test23Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test23Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test2301Cmd = Button(self, textvariable=self.test2301Text,command=self.test2301Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test2301Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 24
    rowIndex += 1
    self.test24Cmd = Button(self, textvariable=self.test24Text,command=self.test24Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test24Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test2401Cmd = Button(self, textvariable=self.test2401Text,command=self.test2401Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test2401Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 25
    rowIndex += 1
    self.test25Cmd = Button(self, textvariable=self.test25Text,command=self.test25Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test25Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test2501Cmd = Button(self, textvariable=self.test2501Text,command=self.test2501Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test2501Cmd.grid(row=rowIndex,column=1,sticky='w')
    self.test2502Cmd = Button(self, textvariable=self.test2502Text,command=self.test2502Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test2502Cmd.grid(row=rowIndex,column=2,sticky='w')

    # Test 26
    rowIndex += 1
    self.test26Cmd = Button(self, textvariable=self.test26Text,command=self.test26Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test26Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test2601Cmd = Button(self, textvariable=self.test2601Text,command=self.test2601Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test2601Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 27
    rowIndex += 1
    self.test27Cmd = Button(self, textvariable=self.test27Text,command=self.test27Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test27Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test2701Cmd = Button(self, textvariable=self.test2701Text,command=self.test2701Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test2701Cmd.grid(row=rowIndex,column=1,sticky='w')
    self.test2702Cmd = Button(self, textvariable=self.test2702Text,command=self.test2702Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test2702Cmd.grid(row=rowIndex,column=2,sticky='w')

    # Test 28
    rowIndex += 1
    self.test28Cmd = Button(self, textvariable=self.test28Text,command=self.test28Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test28Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test2801Cmd = Button(self, textvariable=self.test2801Text,command=self.test2801Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test2801Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 29
    rowIndex += 1
    self.test29Cmd = Button(self, textvariable=self.test29Text,command=self.test29Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test29Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test2901Cmd = Button(self, textvariable=self.test2901Text,command=self.test2901Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test2901Cmd.grid(row=rowIndex,column=1,sticky='w')
    self.test2902Cmd = Button(self, textvariable=self.test2902Text,command=self.test2902Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test2902Cmd.grid(row=rowIndex,column=2,sticky='w')

    # Test 30
    rowIndex += 1
    self.test30Cmd = Button(self, textvariable=self.test30Text,command=self.test30Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test30Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test3001Cmd = Button(self, textvariable=self.test3001Text,command=self.test3001Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test3001Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 31
    rowIndex += 1
    self.test31Cmd = Button(self, textvariable=self.test31Text,command=self.test31Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test31Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test3101Cmd = Button(self, textvariable=self.test3101Text,command=self.test3101Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test3101Cmd.grid(row=rowIndex,column=1,sticky='w')
    self.test3102Cmd = Button(self, textvariable=self.test3102Text,command=self.test3102Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test3102Cmd.grid(row=rowIndex,column=2,sticky='w')

    # Test 32
    rowIndex += 1
    self.test32Cmd = Button(self, textvariable=self.test32Text,command=self.test32Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test32Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test3201Cmd = Button(self, textvariable=self.test3201Text,command=self.test3201Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test3201Cmd.grid(row=rowIndex,column=1,sticky='w')
    self.test3202Cmd = Button(self, textvariable=self.test3202Text,command=self.test3202Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test3202Cmd.grid(row=rowIndex,column=2,sticky='w')
    self.test3203Cmd = Button(self, textvariable=self.test3203Text,command=self.test3203Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test3203Cmd.grid(row=rowIndex,column=3,sticky='w')

    # Test 33
    rowIndex += 1
    self.test33Cmd = Button(self, textvariable=self.test33Text,command=self.test33Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test33Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test3301Cmd = Button(self, textvariable=self.test3301Text,command=self.test3301Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test3301Cmd.grid(row=rowIndex,column=1,sticky='w')
    self.test3302Cmd = Button(self, textvariable=self.test3302Text,command=self.test3302Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test3302Cmd.grid(row=rowIndex,column=2,sticky='w')

    # Test 34
    rowIndex += 1
    self.test34Cmd = Button(self, textvariable=self.test34Text,command=self.test34Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test34Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test3401Cmd = Button(self, textvariable=self.test3401Text,command=self.test3401Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test3401Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 35
    rowIndex += 1
    self.test35Cmd = Button(self, textvariable=self.test35Text,command=self.test35Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test35Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test3501Cmd = Button(self, textvariable=self.test3501Text,command=self.test3501Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test3501Cmd.grid(row=rowIndex,column=1,sticky='w')

    # Test 36
    rowIndex += 1
    self.test36Cmd = Button(self, textvariable=self.test36Text,command=self.test36Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test36Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test3601Cmd = Button(self, textvariable=self.test3601Text,command=self.test3601Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test3601Cmd.grid(row=rowIndex,column=1,sticky='w')
    self.test3602Cmd = Button(self, textvariable=self.test3602Text,command=self.test3602Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test3602Cmd.grid(row=rowIndex,column=2,sticky='w')
    self.test3603Cmd = Button(self, textvariable=self.test3603Text,command=self.test3603Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test3603Cmd.grid(row=rowIndex,column=3,sticky='w')
    self.test3604Cmd = Button(self, textvariable=self.test3604Text,command=self.test3604Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test3604Cmd.grid(row=rowIndex,column=4,sticky='w')
    self.test3605Cmd = Button(self, textvariable=self.test3605Text,command=self.test3605Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test3605Cmd.grid(row=rowIndex,column=5,sticky='w')

    # Test 37
    rowIndex += 1
    self.test37Cmd = Button(self, textvariable=self.test37Text,command=self.test37Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test37Cmd.grid(row=rowIndex,column=0,sticky='w')
    self.test3701Cmd = Button(self, textvariable=self.test3701Text,command=self.test3701Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
    self.test3701Cmd.grid(row=rowIndex,column=1,sticky='w')
    self.test3702Cmd = Button(self, textvariable=self.test3702Text,command=self.test3702Cmd__click,height=gridHeight,width=gridWidth,font=("Arial",fontHeight,"bold"))
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

  # Start/Stop
  def test00Cmd__click(self):
    print("<TEST ALL>")
    if self.testingAll:
      return

    # Reset label colours
    self.station19Cmd__click()

    # TODO: Reset labels
    if self.testPart == "4569":
      self.station17Cmd__click()
    else:
      self.station16Cmd__click()
    self.abortSignal = False
    self.testingAll = True


#    self.station01Cmd__click()
    self.test01Cmd__click()
#    self.GT1000.waitForIdle()
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


    print("test00")
    #exit()
  def test0001Cmd__click(self):
    print("test0001")
    exit()
  # Test 1
  def test01Cmd__click(self):
    tChip = 0x3A
    tPin = 0x55
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(15/1000)
    self.GT1000.write_output(tChip,tPin)
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
    tChip = 0x3A
    tPin = 0x55
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(15/1000)
    self.GT1000.write_output(tChip,tPin)
    if self.GT1000.AFB1[rPin]:
      self.test0101Cmd["bg"] = "green"
      self.test0101Cmd["activebackground"] = "green"
    else:
      self.test0101Cmd["bg"] = "red"
      self.test0101Cmd["activebackground"] = "red"
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
    tChip = 0x3A
    tPin = 0x55
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(15/1000)
    self.GT1000.write_output(tChip,tPin)
    if self.GT1000.AFB1[rPin]:
      self.test0101Cmd["bg"] = "green"
      self.test0101Cmd["activebackground"] = "green"
    else:
      self.test0101Cmd["bg"] = "red"
      self.test0101Cmd["activebackground"] = "red"
    #exit()
  def test0301Cmd__click(self):
    print("test0301")

  # Test 4
  def test04Cmd__click(self):
    print("test04")
    tChip = 0x3A
    tPin = 0x55
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(15/1000)
    self.GT1000.write_output(tChip,tPin)
    if self.GT1000.AFB1[rPin]:
      self.test0101Cmd["bg"] = "green"
      self.test0101Cmd["activebackground"] = "green"
    else:
      self.test0101Cmd["bg"] = "red"
      self.test0101Cmd["activebackground"] = "red"
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
    tChip = 0x3A
    tPin = 0x55
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(15/1000)
    self.GT1000.write_output(tChip,tPin)
    if self.GT1000.AFB1[rPin]:
      self.test0101Cmd["bg"] = "green"
      self.test0101Cmd["activebackground"] = "green"
    else:
      self.test0101Cmd["bg"] = "red"
      self.test0101Cmd["activebackground"] = "red"
    #exit()
  def test0501Cmd__click(self):
    print("test0501")

  # Test 6
  def test06Cmd__click(self):
    print("test06")
    tChip = 0x3A
    tPin = 0x55
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(15/1000)
    self.GT1000.write_output(tChip,tPin)
    if self.GT1000.AFB1[rPin]:
      self.test0101Cmd["bg"] = "green"
      self.test0101Cmd["activebackground"] = "green"
    else:
      self.test0101Cmd["bg"] = "red"
      self.test0101Cmd["activebackground"] = "red"
    #exit()
  def test0601Cmd__click(self):
    print("test0601")
  def test0602Cmd__click(self):
    print("test0602")

  # Test 7
  def test07Cmd__click(self):
    print("test07")
    tChip = 0x3A
    tPin = 0x55
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(15/1000)
    self.GT1000.write_output(tChip,tPin)
    if self.GT1000.AFB1[rPin]:
      self.test0101Cmd["bg"] = "green"
      self.test0101Cmd["activebackground"] = "green"
    else:
      self.test0101Cmd["bg"] = "red"
      self.test0101Cmd["activebackground"] = "red"
    #exit()
  def test0701Cmd__click(self):
    print("test0701")

  # Test 8
  def test08Cmd__click(self):
    print("test08")
    tChip = 0x3A
    tPin = 0x55
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(15/1000)
    self.GT1000.write_output(tChip,tPin)
    if self.GT1000.AFB1[rPin]:
      self.test0101Cmd["bg"] = "green"
      self.test0101Cmd["activebackground"] = "green"
    else:
      self.test0101Cmd["bg"] = "red"
      self.test0101Cmd["activebackground"] = "red"
    #exit()
  def test0801Cmd__click(self):
    print("test0801")
  def test0802Cmd__click(self):
    print("test0802")

  # Test 9
  def test09Cmd__click(self):
    print("test09")
    tChip = 0x3A
    tPin = 0x55
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(15/1000)
    self.GT1000.write_output(tChip,tPin)
    if self.GT1000.AFB1[rPin]:
      self.test0101Cmd["bg"] = "green"
      self.test0101Cmd["activebackground"] = "green"
    else:
      self.test0101Cmd["bg"] = "red"
      self.test0101Cmd["activebackground"] = "red"
    #exit()
  def test0901Cmd__click(self):
    print("test0901")

  # Test 10
  def test10Cmd__click(self):
    print("test10")
    tChip = 0x3A
    tPin = 0x55
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(15/1000)
    self.GT1000.write_output(tChip,tPin)
    if self.GT1000.AFB1[rPin]:
      self.test0101Cmd["bg"] = "green"
      self.test0101Cmd["activebackground"] = "green"
    else:
      self.test0101Cmd["bg"] = "red"
      self.test0101Cmd["activebackground"] = "red"
    #exit()
  def test1001Cmd__click(self):
    print("test1001")

  # Test 11
  def test11Cmd__click(self):
    print("test11")
    tChip = 0x3A
    tPin = 0x55
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(15/1000)
    self.GT1000.write_output(tChip,tPin)
    if self.GT1000.AFB1[rPin]:
      self.test0101Cmd["bg"] = "green"
      self.test0101Cmd["activebackground"] = "green"
    else:
      self.test0101Cmd["bg"] = "red"
      self.test0101Cmd["activebackground"] = "red"
    #exit()
  def test1101Cmd__click(self):
    print("test1101")
  def test1102Cmd__click(self):
    print("test1102")
  def test1103Cmd__click(self):
    print("test1103")

  # Test 12
  def test12Cmd__click(self):
    print("test12")
    tChip = 0x3A
    tPin = 0x55
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(15/1000)
    self.GT1000.write_output(tChip,tPin)
    if self.GT1000.AFB1[rPin]:
      self.test0101Cmd["bg"] = "green"
      self.test0101Cmd["activebackground"] = "green"
    else:
      self.test0101Cmd["bg"] = "red"
      self.test0101Cmd["activebackground"] = "red"
    #exit()
  def test1201Cmd__click(self):
    print("test1201")

  # Test 13
  def test13Cmd__click(self):
    print("test13")
    tChip = 0x3A
    tPin = 0x55
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(15/1000)
    self.GT1000.write_output(tChip,tPin)
    if self.GT1000.AFB1[rPin]:
      self.test0101Cmd["bg"] = "green"
      self.test0101Cmd["activebackground"] = "green"
    else:
      self.test0101Cmd["bg"] = "red"
      self.test0101Cmd["activebackground"] = "red"
    #exit()
  def test1301Cmd__click(self):
    print("test1301")

  # Test 14
  def test14Cmd__click(self):
    print("test14")
    tChip = 0x3A
    tPin = 0x55
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(15/1000)
    self.GT1000.write_output(tChip,tPin)
    if self.GT1000.AFB1[rPin]:
      self.test0101Cmd["bg"] = "green"
      self.test0101Cmd["activebackground"] = "green"
    else:
      self.test0101Cmd["bg"] = "red"
      self.test0101Cmd["activebackground"] = "red"
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
    tChip = 0x3A
    tPin = 0x55
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(15/1000)
    self.GT1000.write_output(tChip,tPin)
    if self.GT1000.AFB1[rPin]:
      self.test0101Cmd["bg"] = "green"
      self.test0101Cmd["activebackground"] = "green"
    else:
      self.test0101Cmd["bg"] = "red"
      self.test0101Cmd["activebackground"] = "red"
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
    tChip = 0x3A
    tPin = 0x55
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(15/1000)
    self.GT1000.write_output(tChip,tPin)
    if self.GT1000.AFB1[rPin]:
      self.test0101Cmd["bg"] = "green"
      self.test0101Cmd["activebackground"] = "green"
    else:
      self.test0101Cmd["bg"] = "red"
      self.test0101Cmd["activebackground"] = "red"
    #exit()
  def test1601Cmd__click(self):
    print("test1601")

  # Test 17
  def test17Cmd__click(self):
    print("test17")
    tChip = 0x3A
    tPin = 0x55
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(15/1000)
    self.GT1000.write_output(tChip,tPin)
    if self.GT1000.AFB1[rPin]:
      self.test0101Cmd["bg"] = "green"
      self.test0101Cmd["activebackground"] = "green"
    else:
      self.test0101Cmd["bg"] = "red"
      self.test0101Cmd["activebackground"] = "red"
    #exit()
  def test1701Cmd__click(self):
    print("test1701")

  # Test 18
  def test18Cmd__click(self):
    print("test18")
    tChip = 0x3A
    tPin = 0x55
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(15/1000)
    self.GT1000.write_output(tChip,tPin)
    if self.GT1000.AFB1[rPin]:
      self.test0101Cmd["bg"] = "green"
      self.test0101Cmd["activebackground"] = "green"
    else:
      self.test0101Cmd["bg"] = "red"
      self.test0101Cmd["activebackground"] = "red"
    #exit()
  def test1801Cmd__click(self):
    print("test1801")

  # Test 19
  def test19Cmd__click(self):
    print("test19")
    tChip = 0x3A
    tPin = 0x55
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(15/1000)
    self.GT1000.write_output(tChip,tPin)
    if self.GT1000.AFB1[rPin]:
      self.test0101Cmd["bg"] = "green"
      self.test0101Cmd["activebackground"] = "green"
    else:
      self.test0101Cmd["bg"] = "red"
      self.test0101Cmd["activebackground"] = "red"
    #exit()
  def test1901Cmd__click(self):
    print("test1901")

  # Test 20
  def test20Cmd__click(self):
    print("test20")
    tChip = 0x3A
    tPin = 0x55
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(15/1000)
    self.GT1000.write_output(tChip,tPin)
    if self.GT1000.AFB1[rPin]:
      self.test0101Cmd["bg"] = "green"
      self.test0101Cmd["activebackground"] = "green"
    else:
      self.test0101Cmd["bg"] = "red"
      self.test0101Cmd["activebackground"] = "red"
    #exit()
  def test2001Cmd__click(self):
    print("test2001")

  # Test 21
  def test21Cmd__click(self):
    print("test21")
    tChip = 0x3A
    tPin = 0x55
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(15/1000)
    self.GT1000.write_output(tChip,tPin)
    if self.GT1000.AFB1[rPin]:
      self.test0101Cmd["bg"] = "green"
      self.test0101Cmd["activebackground"] = "green"
    else:
      self.test0101Cmd["bg"] = "red"
      self.test0101Cmd["activebackground"] = "red"
    #exit()
  def test2101Cmd__click(self):
    print("test2101")

  # Test 22
  def test22Cmd__click(self):
    print("test22")
    tChip = 0x3A
    tPin = 0x55
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(15/1000)
    self.GT1000.write_output(tChip,tPin)
    if self.GT1000.AFB1[rPin]:
      self.test0101Cmd["bg"] = "green"
      self.test0101Cmd["activebackground"] = "green"
    else:
      self.test0101Cmd["bg"] = "red"
      self.test0101Cmd["activebackground"] = "red"
    #exit()
  def test2201Cmd__click(self):
    print("test2201")

  # Test 23
  def test23Cmd__click(self):
    print("test23")
    tChip = 0x3A
    tPin = 0x55
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(15/1000)
    self.GT1000.write_output(tChip,tPin)
    if self.GT1000.AFB1[rPin]:
      self.test0101Cmd["bg"] = "green"
      self.test0101Cmd["activebackground"] = "green"
    else:
      self.test0101Cmd["bg"] = "red"
      self.test0101Cmd["activebackground"] = "red"
    #exit()
  def test2301Cmd__click(self):
    print("test2301")

  # Test 24
  def test24Cmd__click(self):
    print("test24")
    tChip = 0x3A
    tPin = 0x55
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(15/1000)
    self.GT1000.write_output(tChip,tPin)
    if self.GT1000.AFB1[rPin]:
      self.test0101Cmd["bg"] = "green"
      self.test0101Cmd["activebackground"] = "green"
    else:
      self.test0101Cmd["bg"] = "red"
      self.test0101Cmd["activebackground"] = "red"
    #exit()
  def test2401Cmd__click(self):
    print("test2401")

  # Test 25
  def test25Cmd__click(self):
    print("test25")
    tChip = 0x3A
    tPin = 0x55
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(15/1000)
    self.GT1000.write_output(tChip,tPin)
    if self.GT1000.AFB1[rPin]:
      self.test0101Cmd["bg"] = "green"
      self.test0101Cmd["activebackground"] = "green"
    else:
      self.test0101Cmd["bg"] = "red"
      self.test0101Cmd["activebackground"] = "red"
    #exit()
  def test2501Cmd__click(self):
    print("test2501")
  def test2502Cmd__click(self):
    print("test2502")

  # Test 26
  def test26Cmd__click(self):
    print("test26")
    tChip = 0x3A
    tPin = 0x55
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(15/1000)
    self.GT1000.write_output(tChip,tPin)
    if self.GT1000.AFB1[rPin]:
      self.test0101Cmd["bg"] = "green"
      self.test0101Cmd["activebackground"] = "green"
    else:
      self.test0101Cmd["bg"] = "red"
      self.test0101Cmd["activebackground"] = "red"
    #exit()
  def test2601Cmd__click(self):
    print("test2601")

  # Test 27
  def test27Cmd__click(self):
    print("test27")
    tChip = 0x3A
    tPin = 0x55
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(15/1000)
    self.GT1000.write_output(tChip,tPin)
    if self.GT1000.AFB1[rPin]:
      self.test0101Cmd["bg"] = "green"
      self.test0101Cmd["activebackground"] = "green"
    else:
      self.test0101Cmd["bg"] = "red"
      self.test0101Cmd["activebackground"] = "red"
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
    tChip = 0x3A
    tPin = 0x55
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(15/1000)
    self.GT1000.write_output(tChip,tPin)
    if self.GT1000.AFB1[rPin]:
      self.test0101Cmd["bg"] = "green"
      self.test0101Cmd["activebackground"] = "green"
    else:
      self.test0101Cmd["bg"] = "red"
      self.test0101Cmd["activebackground"] = "red"
    #exit()
  def test2801Cmd__click(self):
    print("test2801")
  def test2802Cmd__click(self):
    print("test2802")

  # Test 29
  def test29Cmd__click(self):
    print("test29")
    tChip = 0x3A
    tPin = 0x55
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(15/1000)
    self.GT1000.write_output(tChip,tPin)
    if self.GT1000.AFB1[rPin]:
      self.test0101Cmd["bg"] = "green"
      self.test0101Cmd["activebackground"] = "green"
    else:
      self.test0101Cmd["bg"] = "red"
      self.test0101Cmd["activebackground"] = "red"
    #exit()
  def test2901Cmd__click(self):
    print("test2901")
  def test2902Cmd__click(self):
    print("test2902")

  # Test 30
  def test30Cmd__click(self):
    print("test30")
    tChip = 0x3A
    tPin = 0x55
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(15/1000)
    self.GT1000.write_output(tChip,tPin)
    if self.GT1000.AFB1[rPin]:
      self.test0101Cmd["bg"] = "green"
      self.test0101Cmd["activebackground"] = "green"
    else:
      self.test0101Cmd["bg"] = "red"
      self.test0101Cmd["activebackground"] = "red"
    #exit()
  def test3001Cmd__click(self):
    print("test3001")

  # Test 31
  def test31Cmd__click(self):
    print("test31")
    tChip = 0x3A
    tPin = 0x55
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(15/1000)
    self.GT1000.write_output(tChip,tPin)
    if self.GT1000.AFB1[rPin]:
      self.test0101Cmd["bg"] = "green"
      self.test0101Cmd["activebackground"] = "green"
    else:
      self.test0101Cmd["bg"] = "red"
      self.test0101Cmd["activebackground"] = "red"
    #exit()
  def test3101Cmd__click(self):
    print("test3101")
  def test3102Cmd__click(self):
    print("test3102")

  # Test 32
  def test32Cmd__click(self):
    print("test32")
    tChip = 0x3A
    tPin = 0x55
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(15/1000)
    self.GT1000.write_output(tChip,tPin)
    if self.GT1000.AFB1[rPin]:
      self.test0101Cmd["bg"] = "green"
      self.test0101Cmd["activebackground"] = "green"
    else:
      self.test0101Cmd["bg"] = "red"
      self.test0101Cmd["activebackground"] = "red"
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
    tChip = 0x3A
    tPin = 0x55
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(15/1000)
    self.GT1000.write_output(tChip,tPin)
    if self.GT1000.AFB1[rPin]:
      self.test0101Cmd["bg"] = "green"
      self.test0101Cmd["activebackground"] = "green"
    else:
      self.test0101Cmd["bg"] = "red"
      self.test0101Cmd["activebackground"] = "red"
    #exit()
  def test3301Cmd__click(self):
    print("test3301")
  def test3302Cmd__click(self):
    print("test3302")

  # Test 34
  def test34Cmd__click(self):
    print("test34")
    tChip = 0x3A
    tPin = 0x55
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(15/1000)
    self.GT1000.write_output(tChip,tPin)
    if self.GT1000.AFB1[rPin]:
      self.test0101Cmd["bg"] = "green"
      self.test0101Cmd["activebackground"] = "green"
    else:
      self.test0101Cmd["bg"] = "red"
      self.test0101Cmd["activebackground"] = "red"
    #exit()
  def test3401Cmd__click(self):
    print("test3401")

  # Test 35
  def test35Cmd__click(self):
    print("test35")
    tChip = 0x3A
    tPin = 0x55
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(15/1000)
    self.GT1000.write_output(tChip,tPin)
    if self.GT1000.AFB1[rPin]:
      self.test0101Cmd["bg"] = "green"
      self.test0101Cmd["activebackground"] = "green"
    else:
      self.test0101Cmd["bg"] = "red"
      self.test0101Cmd["activebackground"] = "red"
    #exit()
  def test3501Cmd__click(self):
    print("test3501")

  # Test 36
  def test36Cmd__click(self):
    print("test36")
    tChip = 0x3A
    tPin = 0x55
    rPin = 0x08

    print("Output to ACM1.1, expect AFB1.E3")
    self.GT1000.setBankByPin(16)
    time.sleep(15/1000)
    self.GT1000.write_output(tChip,tPin)
    if self.GT1000.AFB1[rPin]:
      self.test0101Cmd["bg"] = "green"
      self.test0101Cmd["activebackground"] = "green"
    else:
      self.test0101Cmd["bg"] = "red"
      self.test0101Cmd["activebackground"] = "red"
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
    #exit()
  def test3701Cmd__click(self):
    print("test3701")
  def test3702Cmd__click(self):
    print("test3702")


  def station01Cmd__click(self):
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
