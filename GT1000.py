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
  CHIP38 = 0x38
  CHIP001 = 0x39
  CHIP39 = 0x39
  CHIP010 = 0x3a
  CHIP3A = 0x3a
  CHIP011 = 0x3b
  CHIP3B = 0x3b
  CHIP100 = 0x3c
  CHIP3C = 0x3c
  CHIP101 = 0x3d
  CHIP3D = 0x3d
  CHIP110 = 0x3e
  CHIP3E = 0x3e
  CHIP111 = 0x3f
  CHIP3F = 0x3f
  CHIPS = [CHIP000,CHIP001,CHIP010,CHIP011,CHIP100,CHIP101,CHIP110,CHIP111]
  INCHIPS = [CHIP000]
  OUTCHIPS = [CHIP010,CHIP011,CHIP100,CHIP110]

  # Bank selects
  BANK1 = 21
  BANK2 = 20
  BANK3 = 16
  BANK4 = 7
  BANKS = [BANK1,BANK2,BANK3]

  # GPIO Inputs/Outputs
  EXT_IN_START = 6
  EXT_IN_ABORT = 13
  EXT_IN_PART2 = 19
  EXT_IN_CAMOK = 26

  EXT_OUT_INTEST = 23
  EXT_OUT_LATCHRELEASE = 14
  EXT_OUT_START = 23
  EXT_OUT_ABORT = 18
  EXT_OUT_CAMTRIGGER = 8
  EXT_OUT_CAMCLK = 15
  EXT_OUT_CAMDATA = 24

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
  GT_CameraOk = False
  GT_CameraOP2 = False
  GT_CameraOP3 = False

  LED_L = [0,0,0,0]
  HELMET = [0,0,0,0]
  LED_R = [0,0,0,0]
  PARTICULE = [0,0,0,0]
  AFB2 = [0,0,0,0,0,0,0,0,0]
  SNS = [0,0,0]
  ACM = [0,0,0,0,0,0,\
          0,0,0,0,0,0,0,0,0,0,0,0,0,\
          0,0,0,0,0,0,0,0,0,0]
  POSTNEG = 0
  POSTPOS = 0
  POSTACCPOS = 0
  WIPER = [0,0,0,0,0]
  LED_HOOD = [0,0,0,0,0]
  LED_BUMPER = [0,0,0,0,0,0,0]
  LED_ROOF = [0,0,0,0,0,0,0]
  DLC1 = [0,0,0,0,0,0,0]
  DLC2 = [0,0,0,0,0,0,0]
  CHASE_1 = [0,0,0,0,0,0,0]
  KEY_PAD = [0,0,0,0,0,0,0]
  CHASE_2 = [0,0,0,0,0,0,0]
  AFB1 = [0,0,0,0,0,0,\
          0,0,0,0,0,0,\
          0,0,0,0,0,0,\
          0,0,0,0,0,0,\
          0,0,0,0,0,0,\
          0,0,0,0,0,0,0]
  GND = [0,0,0,0,0,0,0,0,0]
  S1X = [0,0,0]
  SXX = [0,0,0,0,0,0,0,0,0,0,0]
  WASHER = [0,0,0]
  SW_1 = [0,0,0,0,0,0,0,0,0]
  PWR_FLIP = [0,0,0]
  CHASE_3 = [0,0,0,0,0,0,0]


  GTchip0int = [0,0,0]
  GTchip1int = [0,0,0]
  GTchip2int = [0,0,0]
  GTchip3int = [0,0,0]
  GTchip4int = [0,0,0]
  GTchip5int = [0,0,0]
  GTchip6int = [0,0,0]
  GTchip7int = [0,0,0]
  GTchip8int = [0,0,0]

  GTchip38int = [0,0,0]
  GTchip39int = [0,0,0]
  GTchip3Aint = [0,0,0]
  GTchip3Bint = [0,0,0]
  GTchip3Cint = [0,0,0]
  GTchip3Dint = [0,0,0]
  GTchip3Eint = [0,0,0]
  GTchip3Fint = [0,0,0]

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
    GPIO.setup(self.EXT_IN_CAMOK, GPIO.IN)

    GPIO.setup(self.EXT_OUT_START, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(self.EXT_OUT_ABORT, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(self.EXT_OUT_LATCHRELEASE, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(self.EXT_OUT_CAMTRIGGER, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(self.EXT_OUT_CAMCLK, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(self.EXT_OUT_CAMDATA, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(self.BANKS[0], GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(self.BANKS[1], GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(self.BANKS[2], GPIO.OUT, initial=GPIO.LOW)
    self.setBankByPin(16)
    time.sleep(30/1000)
    self.write_output(0x38,0)
    self.write_output(0x39,0)
    self.write_output(0x3A,0)
    self.write_output(0x3B,0)
    self.write_output(0x3C,0)
    self.write_output(0x3D,0)
#    GPIO.setup(self.BANKS[3], GPIO.OUT, initial=GPIO.LOW)
    print("[end call] __GPIO_Setup()")

  def getLatchState(self):
    return GPIO.input(self.EXT_OUT_LATCHRELEASE)

  def waitForIdle(self):
    toTim = time.time()
    while (time.time() - toTim) < 2:
      self.read_inputs()
      if not self.GT_InTest:
        time.sleep(0.5)
        break

  def read_inputs(self):
    print("[call] read_inputs()")

    # Get GPIO Information
    #self.GT_Start = (GPIO.input(self.EXT_IN_START) == 0)
    #self.GT_Abort = (GPIO.input(self.EXT_IN_ABORT) == 0)
    #self.GT_PartSelect = (GPIO.input(self.EXT_IN_PART2) == 0)
    #self.GT_CameraOk = (GPIO.input(self.EXT_IN_CAMOK) == 0)
    self.GT_Start = False
    self.GT_Abort = False
    self.GT_PartSelect = False
    self.GT_CameraOk = False

    print(">>Start: ", self.GT_Start, "  Part Select: ", self.GT_PartSelect, "  Abort: ",self.GT_Abort)


    # Get PIA data
    #  Installed MUX relays are DS2E-M-DC12V-R: Operate time 10ms, release time 5ms
    i = 0
    for b in self.BANKS:
      self.setBankByPin(b)
      time.sleep(30/1000)
      try:
        self.GTchip38int[i] = self.__I2C.read_byte(self.CHIP38)
      except Exception as e:
        print("!!! ", str(e), " !!!")
        pass
      try:
        self.GTchip39int[i] = self.__I2C.read_byte(self.CHIP39)
      except Exception as e:
        print("!!! ", str(e), " !!!")
        pass
      try:
        self.GTchip3Aint[i] = self.__I2C.read_byte(self.CHIP3A)
      except Exception as e:
        print("!!! ", str(e), " !!!")
        pass
      try:
        self.GTchip3Bint[i] = self.__I2C.read_byte(self.CHIP3B)
      except Exception as e:
        print("!!! ", str(e), " !!!")
        pass
      try:
        self.GTchip3Cint[i] = self.__I2C.read_byte(self.CHIP3C)
      except Exception as e:
        print("!!! ", str(e), " !!!")
        pass
      try:
        self.GTchip3Dint[i] = self.__I2C.read_byte(self.CHIP3D)
      except Exception as e:
        print("!!! ", str(e), " !!!")
        pass
      try:
        self.GTchip3Eint[i] = self.__I2C.read_byte(self.CHIP3E)
      except Exception as e:
        print("!!! ", str(e), " !!!")
        pass
      try:
        self.GTchip3Fint[i] = self.__I2C.read_byte(self.CHIP3F)
      except Exception as e:
        print("!!! ", str(e), " !!!")
        pass
      try:
        i += 1
      except Exception as e:
        print("!!! ", str(e), " !!!")
        pass

    print("0x38: ", self.GTchip38int[0], "/", self.GTchip38int[1], "/", self.GTchip38int[2])
    print("0x39: ", self.GTchip39int[0], "/", self.GTchip39int[1], "/", self.GTchip39int[2])
    print("0x3A: ", self.GTchip3Aint[0], "/", self.GTchip3Aint[1], "/", self.GTchip3Aint[2])
    print("0x3B: ", self.GTchip3Bint[0], "/", self.GTchip3Bint[1], "/", self.GTchip3Bint[2])
    print("0x3C: ", self.GTchip3Cint[0], "/", self.GTchip3Cint[1], "/", self.GTchip3Cint[2])
    print("0x3D: ", self.GTchip3Dint[0], "/", self.GTchip3Dint[1], "/", self.GTchip3Dint[2])
    print("0x3E: ", self.GTchip3Eint[0], "/", self.GTchip3Eint[1], "/", self.GTchip3Eint[2])
    print("0x3F: ", self.GTchip3Fint[0], "/", self.GTchip3Fint[1], "/", self.GTchip3Fint[2])
    # Bank 0 = 21;  Bank 1 = 20;  Bank 2 = 16
    ## Posts  @  *  *
    ##        -  +  A+
    self.POSTNEG = self.GTchip3Dint[1] & 0x20
    self.POSTPOS = self.GTchip3Dint[2] & 0x02
    self.POSTACCPOS = self.GTchip3Dint[2] & 0x01

    # LED_L    @@@
    # (Shares connector with HELMET_FAN)
    self.LED_L[1] = self.GTchip3Aint[1] & 0x01
    self.LED_L[2] = self.GTchip3Aint[1] & 0x02
    self.LED_L[3] = self.GTchip3Aint[1] & 0x04
    self.HELMET[1] = self.GTchip3Aint[1] & 0x01
    self.HELMET[2] = self.GTchip3Aint[1] & 0x02
    self.HELMET[3] = self.GTchip3Aint[1] & 0x04

    # LED_R    @@@
    # (Shares connector with PARTICULE)
    self.LED_R[1] = self.GTchip3Dint[0] & 0x01
    self.LED_R[2] = self.GTchip3Dint[0] & 0x02
    self.LED_R[3] = self.GTchip3Dint[0] & 0x04
    self.PARTICULE[1] = self.GTchip3Dint[0] & 0x01
    self.PARTICULE[2] = self.GTchip3Dint[0] & 0x02
    self.PARTICULE[3] = self.GTchip3Dint[0] & 0x04

    # AFB2    @@@*  8765
    #         @*@*  1234
    self.AFB2[1] = self.GTchip3Cint[0] & 0x04
    self.AFB2[2] = self.GTchip3Cint[2] & 0x01
    self.AFB2[3] = self.GTchip3Cint[0] & 0x08
    self.AFB2[4] = self.GTchip3Cint[2] & 0x02
    self.AFB2[5] = self.GTchip3Cint[2] & 0x04
    self.AFB2[6] = self.GTchip3Cint[0] & 0x10
    self.AFB2[7] = self.GTchip3Cint[0] & 0x20
    self.AFB2[8] = self.GTchip3Cint[0] & 0x40

    # WIPER   @@  23
    #         @@  14
    self.WIPER[1] = self.GTchip3Aint[1] & 0x08
    self.WIPER[2] = self.GTchip3Aint[1] & 0x10
    self.WIPER[3] = self.GTchip3Aint[1] & 0x20
    self.WIPER[4] = self.GTchip3Aint[1] & 0x40

    # WASHER  @@  21
    self.WASHER[1] = self.GTchip3Fint[1] & 0x01
    self.WASHER[2] = self.GTchip3Fint[1] & 0x02

    # SNS     @@  12
    self.SNS[2] = self.GTchip3Cint[0] & 0x01
    self.SNS[1] = self.GTchip3Cint[0] & 0x02


    # AFB1
    self.AFB1[4] = self.GTchip39int[1] & 0x10  #A4
    self.AFB1[6] = self.GTchip3Bint[1] & 0x02  #A6
    self.AFB1[10] = self.GTchip39int[1] & 0x08  #B4
    self.AFB1[11] = self.GTchip3Bint[2] & 0x80  #B5
    self.AFB1[12] = self.GTchip3Bint[2] & 0x40  #B6
    self.AFB1[13] = self.GTchip3Bint[2] & 0x20  #C1
    self.AFB1[14] = self.GTchip3Bint[2] & 0x10  #C2
    self.AFB1[15] = self.GTchip3Bint[1] & 0x01  #C3
    self.AFB1[16] = self.GTchip3Bint[2] & 0x08  #C4
    self.AFB1[18] = self.GTchip39int[1] & 0x04  #C6
    self.AFB1[19] = self.GTchip3Bint[1] & 0x04  #D1
    self.AFB1[21] = self.GTchip3Bint[2] & 0x04  #D3
    self.AFB1[22] = self.GTchip39int[1] & 0x02  #D4
    self.AFB1[23] = self.GTchip39int[1] & 0x01  #D5
    self.AFB1[24] = self.GTchip3Bint[2] & 0x02  #D6
    self.AFB1[25] = self.GTchip3Bint[2] & 0x01  #E1
    self.AFB1[26] = self.GTchip38int[1] & 0x40  #E2
    self.AFB1[27] = self.GTchip38int[1] & 0x20  #E3
    self.AFB1[28] = self.GTchip38int[1] & 0x10  #E4
    self.AFB1[29] = self.GTchip38int[1] & 0x08  #E5
    self.AFB1[30] = self.GTchip38int[1] & 0x04  #E6
    self.AFB1[31] = self.GTchip39int[1] & 0x20  #F1
    self.AFB1[32] = self.GTchip39int[1] & 0x40  #F2
    self.AFB1[35] = self.GTchip38int[1] & 0x02  #F5
    self.AFB1[36] = self.GTchip38int[1] & 0x01  #F6



    # Bank 0 = 21;  Bank 1 = 20;  Bank 2 = 16

    # ACM
    self.ACM[1] = self.GTchip39int[2] & 0x04 # fb
    self.ACM[2] = self.GTchip39int[2] & 0x08 # f7
    self.ACM[3] = self.GTchip39int[2] & 0x10 # ef
    self.ACM[4] = self.GTchip39int[2] & 0x80 # 7f
    self.ACM[5] = self.GTchip39int[2] & 0x20 # df
    self.ACM[6] = self.GTchip39int[2] & 0x40 # bf
    self.ACM[7] = self.GTchip39int[2] & 0x01 # fe
    self.ACM[8] = self.GTchip39int[2] & 0x02 # fd

    self.ACM[9] = self.GTchip38int[2] & 0x04
    self.ACM[10] = self.GTchip38int[2] & 0x08
    self.ACM[11] = self.GTchip38int[2] & 0x10
    self.ACM[12] = self.GTchip38int[2] & 0x80
    self.ACM[13] = self.GTchip38int[2] & 0x20
    self.ACM[14] = self.GTchip38int[2] & 0x40
    self.ACM[15] = self.GTchip38int[2] & 0x01
#    self.ACM[16] = self.GTchip38int[2] & 0x02 

    self.ACM[16] = self.GTchip3Aint[2] & 0x04
    self.ACM[17] = self.GTchip3Aint[2] & 0x08
    self.ACM[18] = self.GTchip3Aint[2] & 0x10
    self.ACM[19] = self.GTchip3Aint[2] & 0x80
    self.ACM[20] = self.GTchip3Aint[2] & 0x20
    self.ACM[21] = self.GTchip3Aint[2] & 0x40
    self.ACM[22] = self.GTchip3Aint[2] & 0x01
    self.ACM[23] = self.GTchip3Aint[2] & 0x02

    self.ACM[24] = self.GTchip3Cint[2] & 0x08
    self.ACM[25] = self.GTchip3Cint[2] & 0x10
    self.ACM[26] = self.GTchip3Cint[2] & 0x20
    self.ACM[27] = self.GTchip3Cint[2] & 0x40
    self.ACM[28] = self.GTchip3Cint[2] & 0x80

    # CHASE_3  @@  34
    #          @@  25
    #          @@  16
    self.CHASE_3[1] = self.GTchip3Eint[1] & 0x01
    self.CHASE_3[2] = self.GTchip3Eint[1] & 0x02
    self.CHASE_3[3] = self.GTchip3Eint[1] & 0x04
    self.CHASE_3[4] = self.GTchip3Eint[1] & 0x08
    self.CHASE_3[5] = self.GTchip3Eint[1] & 0x10
    self.CHASE_3[6] = self.GTchip3Eint[1] & 0x20

    # DLC1      **  43
    #           *@  52
    #           @@  61
    self.DLC1[1] = self.GTchip3Dint[1] & 0x01
    self.DLC1[2] = self.GTchip3Dint[1] & 0x02
    self.DLC1[3] = self.GTchip3Dint[2] & 0x04
    self.DLC1[4] = self.GTchip3Dint[2] & 0x08
    self.DLC1[5] = self.GTchip3Dint[2] & 0x10
    self.DLC1[6] = self.GTchip3Dint[1] & 0x04

    # DLC2      @@  34
    #           @@  25
    #           @@  16
    # (Shares with CHASE_1)
    self.DLC2[1] = self.GTchip3Cint[1] & 0x04
    self.DLC2[2] = self.GTchip3Cint[1] & 0x08
    self.DLC2[3] = self.GTchip3Cint[1] & 0x10
    self.DLC2[4] = self.GTchip3Cint[1] & 0x20
    self.DLC2[5] = self.GTchip3Cint[1] & 0x40
    self.DLC2[6] = self.GTchip3Cint[1] & 0x80
    self.CHASE_1[1] = self.GTchip3Cint[1] & 0x04
    self.CHASE_1[2] = self.GTchip3Cint[1] & 0x08
    self.CHASE_1[3] = self.GTchip3Cint[1] & 0x10
    self.CHASE_1[4] = self.GTchip3Cint[1] & 0x20
    self.CHASE_1[5] = self.GTchip3Cint[1] & 0x40
    self.CHASE_1[6] = self.GTchip3Cint[1] & 0x80

    # KEY_PAD   34
    #           25
    #           16
    # (Shares with CHASE_2)
    self.KEY_PAD[1] = self.GTchip3Fint[1] & 0x04
    self.KEY_PAD[2] = self.GTchip3Fint[1] & 0x08
    self.KEY_PAD[3] = self.GTchip3Fint[1] & 0x10
    self.KEY_PAD[4] = self.GTchip3Fint[1] & 0x20
    self.KEY_PAD[5] = self.GTchip3Fint[1] & 0x40
    self.KEY_PAD[6] = self.GTchip3Fint[1] & 0x80
    self.CHASE_2[1] = self.GTchip3Fint[1] & 0x04
    self.CHASE_2[2] = self.GTchip3Fint[1] & 0x08
    self.CHASE_2[3] = self.GTchip3Fint[1] & 0x10
    self.CHASE_2[4] = self.GTchip3Fint[1] & 0x20
    self.CHASE_2[5] = self.GTchip3Fint[1] & 0x40
    self.CHASE_2[6] = self.GTchip3Fint[1] & 0x80

    # GND  @@ @@@@  12  3456
    #          @@        87
    self.GND[1] = self.GTchip3Eint[0] & 0x01
    self.GND[2] = self.GTchip3Eint[0] & 0x02
    self.GND[3] = self.GTchip3Eint[0] & 0x04
    self.GND[4] = self.GTchip3Eint[0] & 0x08
    self.GND[5] = self.GTchip3Eint[0] & 0x10
    self.GND[6] = self.GTchip3Eint[0] & 0x20
    self.GND[7] = self.GTchip3Eint[0] & 0x40
    self.GND[8] = self.GTchip3Eint[0] & 0x80

    # S1X    @@  21
    self.S1X[1] = self.GTchip3Fint[0] & 0x02
    self.S1X[2] = self.GTchip3Fint[0] & 0x01

    # S2X    @@!@   1234    TODO: There is a short b/t 3(BK) or ORbk(6)
    #        @!@@   5678
    self.SXX[1] = self.GTchip3Aint[0] & 0x01
    self.SXX[2] = self.GTchip3Aint[0] & 0x02
    self.SXX[3] = self.GTchip3Aint[0] & 0x04
    self.SXX[4] = self.GTchip3Aint[0] & 0x08
    self.SXX[5] = self.GTchip3Aint[0] & 0x10
    self.SXX[6] = self.GTchip3Aint[0] & 0x20
    self.SXX[7] = self.GTchip3Aint[0] & 0x40
    self.SXX[8] = self.GTchip3Aint[0] & 0x80

    # PWR_FLIP    @@  21
    self.PWR_FLIP[1] = self.GTchip3Cint[1] & 0x01
    self.PWR_FLIP[2] = self.GTchip3Cint[1] & 0x02

    # SW_1    @     7
    #         @@@@  8123
    self.SW_1[1] = self.GTchip39int[0] & 0x01
    self.SW_1[2] = self.GTchip39int[0] & 0x02
    self.SW_1[3] = self.GTchip39int[0] & 0x04
    self.SW_1[7] = self.GTchip39int[0] & 0x20
    self.SW_1[8] = self.GTchip39int[0] & 0x40

    # LED_ROOF    @@@  654
    #             @@@  321
    self.LED_ROOF[1] = self.GTchip38int[0] & 0x04
    self.LED_ROOF[2] = self.GTchip38int[0] & 0x02
    self.LED_ROOF[3] = self.GTchip38int[0] & 0x01
    self.LED_ROOF[4] = self.GTchip38int[0] & 0x08
    self.LED_ROOF[5] = self.GTchip38int[0] & 0x10
    self.LED_ROOF[6] = self.GTchip38int[0] & 0x20

    # LED_BUMPER  @@@  654
    #             @!@  321
    self.LED_BUMPER[1] = self.GTchip3Bint[0] & 0x01
    self.LED_BUMPER[2] = self.GTchip3Bint[0] & 0x02
    self.LED_BUMPER[3] = self.GTchip3Bint[0] & 0x04
    self.LED_BUMPER[4] = self.GTchip3Bint[0] & 0x08
    self.LED_BUMPER[5] = self.GTchip3Bint[0] & 0x10
    self.LED_BUMPER[6] = self.GTchip3Bint[0] & 0x20

    # LED_HOOD    @@  42
    #             @@  31
    self.LED_HOOD[1] = self.GTchip3Dint[0] & 0x08
    self.LED_HOOD[2] = self.GTchip3Dint[0] & 0x10
    self.LED_HOOD[4] = self.GTchip3Dint[0] & 0x40
    self.LED_HOOD[3] = self.GTchip3Dint[0] & 0x20

    # Place read in containers
    self.GT_InTest = self.GTchip0int[0] & 0x01
    self.GT_Pass = self.GTchip0int[0] & 0x02
    self.GT_Fail = self.GTchip0int[0] & 0x04
    self.GT_CameraOP2 = self.GTchip0int[0] & 0xF0
    self.GT_CameraOP3 = self.GTchip0int[0] & 0x80


    GPIO.output(self.EXT_OUT_ABORT, self.GT_Abort)
    print(">>In Test: ", self.GT_InTest, "  Pass: ", self.GT_Pass, "  Fail: ", self.GT_Fail)
    print("[end call] read_inputs()")

  def clear_outputs(self):
    self.setBankByPin(16)
    time.sleep(15/1000)
    self.write_output(0x38,0)
    self.write_output(0x39,0)
    self.write_output(0x3A,0)
    self.write_output(0x3B,0)
    self.write_output(0x3C,0)
    self.write_output(0x3D,0)

  def write_output(self, addy, data):
    try:
      print("Writing ", data, " to ", addy)
      self.__I2C.write_byte_data(addy, 1, 255-data)
      time.sleep(5/1000)
      self.read_inputs()
    except Exception as e:
      pass

  def setBank(self, val):
    print("Setting bank ", val)
    for c in self.BANKS:
      GPIO.output(c,0)
    GPIO.output(self.CHIPS[val+1],1)

  def setBankByPin(self, val):
    print("Setting bank ", val)
    for c in self.BANKS:
      GPIO.output(c,0)
    GPIO.output(val,1)
    time.sleep(30/1000)

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
          self.GTchip2int[0] += 128
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
    restarted = False
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
      if ((currtime - startFunction) > 2) and not restarted:
        GPIO.output(self.EXT_OUT_START, 0)
        restarted = True
      if ((currtime - startFunction) > 2.5) and restarted:
        GPIO.output(self.EXT_OUT_START, 1)
      if (currtime - startFunction) > 5:
        print("Tester didn't start")
        GPIO.output(self.EXT_OUT_START, 0)
        return -1
        #self.GT_InTest = True
        #break
    GPIO.output(self.EXT_OUT_START,0)
    print("Tester in test...")
    return 1

  def abortTest(self):
    print("abortTest()")
    GPIO.output(self.EXT_OUT_ABORT, 1)
    sleep(0.8)
    GPIO.output(self.EXT_OUT_ABORT, 0)

  def triggerCamera(self):
    print("[call] triggerCamera()")
    GPIO.output(self.EXT_OUT_CAMTRIGGER, 1)
    time.sleep(0.5)
    GPIO.output(self.EXT_OUT_CAMTRIGGER, 0)
    print("[end call] pulseRelease()")


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


