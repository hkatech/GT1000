import time
import sys
import RPi.GPIO as GPIO
import smbus
import fcntl

class GT1000:
  # PIA Chip references
  I2C_BUS = 1
  __I2C = smbus.SMBus(I2C_BUS)
  CHIP000 = 0x38
  CHIP001 = 0x39
  CHIP010 = 0x3a
  CHIP011 = 0x3b
  CHIP100 = 0x3c
  CHIP101 = 0x3d
  CHIP110 = 0x3e
  CHIP111 = 0x3f
  CHIPS = [CHIP000,CHIP001,CHIP010,CHIP011,CHIP100,CHIP101,CHIP110,CHIP111]
  INCHIPS = [CHIP000]
  OUTCHIPS = [CHIP010,CHIP011,CHIP100,CHIP110]

  # Bank selects
  BANK1 = 21
  BANK2 = 20
  BANK3 = 16
  BANK4 = 7
  BANKS = [BANK1,BANK2,BANK3,BANK4]

  # GPIO Inputs/Outputs
  EXT_IN_START = 6
  EXT_IN_ABORT = 13
  EXT_IN_PART2 = 19

  EXT_OUT_PASS = 8
  EXT_OUT_FAIL = 24
  EXT_OUT_INTEST = 23
  EXT_OUT_LATCHRELEASE = 14
  EXT_OUT_START = 23
  EXT_OUT_ABORT = 18

  GT_Start = False
  GT_Abort = False
  GT_PartSelect = False
  GT_LK = False
  GT_Pass = False
  GT_Fail = False
  GT_InTest = False
  GT_UserOut = False
  GT_LTStart = False
  GT_LTAbort = False

  GTchip0int = [0,0,0]
  GTchip1int = [0,0,0]
  GTchip2int = [0,0,0]
  GTchip3int = [0,0,0]
  GTchip4int = [0,0,0]
  GTchip5int = [0,0,0]
  GTchip6int = [0,0,0]
  GTchip7int = [0,0,0]
  GTchip8int = [0,0,0]

  # Stations
  testStations = [\
    ["Station 1",0x3a,0],\
    ["Station 2",0x3a,1],\
    ["Station 3",0x3a,2],\
    ["Station 4",0x3a,3],\
    ["Station 5",0x3a,4],\
    ["Station 6",0x3a,5],\
    ["Station 7",0x3a,6],\
    ["Station 8",0x3a,7],\
    ["Station 9",0x3b,0],\
    ["Station 10",0x3b,1],\
    ["Station 11",0x3b,2],\
    ["Station 12",0x3b,3],\
    ["Station 13",0x3b,4],\
    ["Station 14",0x3b,5],\
    ["Station 15",0x3b,6],\
    ["Station 16",0x3b,7]]

  stationChips = [\
    CHIP000, CHIP000, CHIP000, CHIP000, CHIP000, \
    CHIP000, CHIP000, CHIP000, CHIP000, CHIP000, \
    CHIP000, CHIP000, CHIP000, CHIP000, CHIP000, \
    CHIP000, CHIP000, CHIP000, CHIP000, CHIP000]


  def __GPIO_Setup(self):
    print("[call] __GPIO_Setup()")
    GPIO.setup(self.EXT_IN_START, GPIO.IN)
    GPIO.setup(self.EXT_IN_ABORT, GPIO.IN)
    GPIO.setup(self.EXT_IN_PART2, GPIO.IN)

    GPIO.setup(self.EXT_OUT_START, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(self.EXT_OUT_ABORT, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(self.EXT_OUT_INTEST, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(self.EXT_OUT_LATCHRELEASE, GPIO.OUT, initial=GPIO.LOW)
    print("[end call] __GPIO_Setup()")

  def getLatchState(self):
    return GPIO.input(self.EXT_OUT_LATCHRELEASE)

  def read_inputs(self):
    print("[call] read_inputs()")
    GT_Start = GPIO.input(self.EXT_IN_START)
    GT_Abort = GPIO.input(self.EXT_IN_ABORT)
    GT_PartSelect = GPIO.input(self.EXT_IN_PART2)
    try:
      self.GTchip0int[0] = self.__I2C.read_byte(self.CHIP000)
      #self.GTchip2int[0] = self.__I2C.read_byte(self.CHIP010)
      #self.GTchip3int[0] = self.__I2C.read_byte(self.CHIP011)
      #self.GTchip4int[0] = self.__I2C.read_byte(self.CHIP100)
      #self.GTchip6int[0] = self.__I2C.read_byte(self.CHIP110)
    except Exception as e:
      print("!!! ", str(e), " !!!")
      pass
    self.GT_InTest = self.GTchip0int[0] & 0x01
    self.GT_Pass = self.GTchip0int[0] & 0x02
    self.GT_Fail = self.GTchip0int[0] & 0x04
    print("[end call] read_inputs()")

  def write_output(self, addy, data):
    self.__I2C.write_byte_data(addy, 1, data)

  def resetAllOutputs(self):
    print("[call] resetAllOutputs()")
    #self.GTchip0int[0] = 0
    #self.GTchip1int[0] = 0
    #self.GTchip2int[0] = 0
    #self.GTchip3int[0] = 0
    #self.GTchip4int[0] = 0
    #self.GTchip5int[0] = 0
    #self.GTchip6int[0] = 0
    #self.GTchip7int[0] = 0
    try:
      for val in self.OUTCHIPS:
        self.write_output(val,0)
    except Exception as e:
      print("!!! ", str(e), " !!!")
      pass
    print("[end call] resetAllOutputs()")

  def enableStations(self, val):
    print("[call] enableStations(", val, ")")
    self.GTchip2int[0] = 0
    self.GTchip3int[0] = 0
    for sval in val:
        if sval == 1:
          self.GTchip2int[0] += 1
        if sval == 2:
          self.GTchip2int[0] += 2
        if sval == 3:
          self.GTchip2int[0] += 4
        if sval == 4:
          self.GTchip2int[0] += 8
        if sval == 5:
          self.GTchip2int[0] += 16
        if sval == 6:
          self.GTchip2int[0] += 32
        if sval == 7:
          self.GTchip2int[0] += 64
        if sval == 8:
          self.GTchip3int[0] += 128
        if sval == 9:
          self.GTchip3int[0] += 1
        if sval == 10:
          self.GTchip3int[0] += 2
        if sval == 11:
          self.GTchip3int[0] += 4
        if sval == 12:
          self.GTchip3int[0] += 8
        if sval == 13:
          self.GTchip3int[0] += 16
        if sval == 14:
          self.GTchip3int[0] += 32
        if sval == 15:
          self.GTchip3int[0] += 64
        if sval == 16:
          self.GTchip3int[0] += 128
    try:
      self.write_output(self.CHIP010,self.GTchip2int[0])
      self.write_output(self.CHIP011,self.GTchip3int[0])
    except Exception as e:
      print("!!! ", str(e), " !!!")
      pass

    print("[end call] enableStations()")

  def startTest(self):
    startFunction = time.time()
    print("startTest() at ", startFunction)
    if self.GT_InTest:
      print("Leak Test already In Test")
      return 0
    print("Setting START high...")
    GPIO.output(self.EXT_OUT_START, 1)
    while not self.GT_InTest:
      currtime = time.time()
      time.sleep(0.2)
      self.read_inputs()
      print(currtime - startFunction)
      if (currtime - startFunction) > 2:
        print("Tester didn't start")
        GPIO.output(self.EXT_OUT_START, 0)
        #return -1
        self.GT_InTest = True
        break
    GPIO.output(self.EXT_OUT_START,0)
    print("Tester in test...")
    return 1

  def abortTest(self):
    print("abortTest()")
    GPIO.output(self.EXT_OUT_ABORT, 1)
    sleep(0.8)
    GPIO.output(self.EXT_OUT_ABORT, 0)

  def pulseRelease(self):
    print("[call] pulseRelease()")
    GPIO.output(self.EXT_OUT_LATCHRELEASE, 1)
    time.sleep(1)
    GPIO.output(self.EXT_OUT_LATCHRELEASE, 0)
    print("[end call] pulseRelease()")

  def latchReleaseEn(self):
    print("Releasing latch")
    GPIO.output(self.EXT_OUT_LATCHRELEASE, 1)

  def latchReleaseDis(self):
    print("Engaging latch")
    GPIO.output(self.EXT_OUT_LATCHRELEASE, 0)

  def __init__(self):
    # Setup the GT1000
    print("< NEW > Initializing GT1000 object")

    # Setup the GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    self.__GPIO_Setup()
    self.resetAllOutputs()
    self.read_inputs()


