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

  # Bank selects
  BANK1 = 21
  BANK2 = 20
  BANK3 = 16
  BANK4 = 7
  BANKS = [BANK1,BANK2,BANK3,BANK4]

  # GPIO Inputs/Outputs
  EXT_IN_START = 13
  EXT_IN_ABORT = 19
  EXT_IN_USER2 = 6
  EXT_IN_LEAK = 26

  EXT_OUT_PASS = 18
  EXT_OUT_FAIL = 15
  EXT_OUT_INTEST = 23
  EXT_OUT_USER1 = 8
  EXT_OUT_START = 18
  EXT_OUT_ABORT = 15

  GT_Start = False
  GT_Abort = False
  GT_UserIn = False
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

  stationChips = [\
    CHIP000, CHIP000, CHIP000, CHIP000, CHIP000, \
    CHIP000, CHIP000, CHIP000, CHIP000, CHIP000, \
    CHIP000, CHIP000, CHIP000, CHIP000, CHIP000, \
    CHIP000, CHIP000, CHIP000, CHIP000, CHIP000]


  def __GPIO_Setup(self):
    print("[call] __GPIO_Setup()")
    GPIO.setup(self.EXT_IN_START, GPIO.IN)
    GPIO.setup(self.EXT_IN_ABORT, GPIO.IN)
    GPIO.setup(self.EXT_IN_USER2, GPIO.IN)
    GPIO.setup(self.EXT_IN_LEAK, GPIO.IN)

    # Pass/Fail map to LTStart/LTFail
    GPIO.setup(self.EXT_OUT_PASS, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(self.EXT_OUT_FAIL, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(self.EXT_OUT_INTEST, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(self.EXT_OUT_USER1, GPIO.OUT, initial=GPIO.LOW)
    print("[end call] __GPIO_Setup()")


  def read_inputs(self):
    print("[call] read_inputs()")
    GT_Start = GPIO.input(self.EXT_IN_START)
    GT_Abort = GPIO.input(self.EXT_IN_ABORT)
    GT_UserIn = GPIO.input(self.EXT_IN_USER2)
    GT_LK = GPIO.input(self.EXT_IN_LEAK)
    try:
      self.GTchip0int[0] = self.__I2C.read_byte(self.CHIP000)
      self.GTchip1int[0] = self.__I2C.read_byte(self.CHIP001)
      self.GTchip2int[0] = self.__I2C.read_byte(self.CHIP010)
      self.GTchip3int[0] = self.__I2C.read_byte(self.CHIP011)
      self.GTchip4int[0] = self.__I2C.read_byte(self.CHIP100)
      self.GTchip5int[0] = self.__I2C.read_byte(self.CHIP101)
      self.GTchip6int[0] = self.__I2C.read_byte(self.CHIP110)
      self.GTchip7int[0] = self.__I2C.read_byte(self.CHIP111)
    except Exception as e:
      print("!!! ", str(e), " !!!")
      pass

    print("[end call] read_inputs()")

  def write_output(self, addy, data):
    self.__I2C.write_byte_data(addy, 1, data)

  def resetAllOutputs(self):
    #self.GTchip0int[0] = 0
    #self.GTchip1int[0] = 0
    #self.GTchip2int[0] = 0
    #self.GTchip3int[0] = 0
    #self.GTchip4int[0] = 0
    #self.GTchip5int[0] = 0
    #self.GTchip6int[0] = 0
    #self.GTchip7int[0] = 0
    for val in self.CHIPS:
      self.write_output(val,0)


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
        return -1
    GPIO.output(self.EXT_OUT_START,0)
    print("Tester in test...")
    return 1

  def abortTest(self):
    print("abortTest()")
    GPIO.output(self.EXT_OUT_ABORT, 1)
    sleep(0.8)
    GPIO.output(self.EXT_OUT_ABORT, 0)

  def __init__(self):
    # Setup the GT1000
    print("< NEW > Initializing GT1000 object")

    # Setup the GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    self.__GPIO_Setup()
    self.read_inputs()
