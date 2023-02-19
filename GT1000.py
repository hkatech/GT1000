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
  CHIPS = [CHIP000,CHIP001,CHIP010,CHIP011,CHIP100]

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

  GT_Start = False
  GT_Abort = False
  GT_UserIn = False
  GT_LK = False
  GT_Pass = False
  GT_Fail = False
  GT_InTest = False
  GT_UserOut = False


  def __GPIO_Setup(self):
    print("[Func] __GPIO_Setup()")
    GPIO.setup(self.EXT_IN_START, GPIO.IN)
    GPIO.setup(self.EXT_IN_ABORT, GPIO.IN)
    GPIO.setup(self.EXT_IN_USER2, GPIO.IN)
    GPIO.setup(self.EXT_IN_LEAK, GPIO.IN)

    GPIO.setup(self.EXT_OUT_PASS, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(self.EXT_OUT_FAIL, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(self.EXT_OUT_INTEST, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(self.EXT_OUT_USER1, GPIO.OUT, initial=GPIO.LOW)


  def read_inputs(self):
    print("[Func] read_inputs()")
    GT_Start = GPIO.input(self.EXT_IN_START)
    GT_Abort = GPIO.input(self.EXT_IN_ABORT)
    GT_UserIn = GPIO.input(self.EXT_IN_USER2)
    GT_LK = GPIO.input(self.EXT_IN_LEAK)

  def __init__(self):
    # Setup the GT1000
    print("< NEW > Initializing GT1000 object")

    # Setup the GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    self.__GPIO_Setup()
    self.read_inputs()
