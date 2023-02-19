import tkinter as tk
from tkinter import *
from GT1000 import GT1000

class debugWindow(Frame):

  def __init__(self, master=None):
    print("<NEW> Initializing debugWindow...")
    Frame.__init__(self,master)
    self.pack(fill=BOTH, expand=1)

    #exitCmd = Button(self, text="Exit", command=self.clickExitCmd, height=2, width=1)
    #exitCmd.place(x=0, y=0)

    q38Cmd = Button(self, text="Read 0x38", command=self.clickQ38Cmd)
    q38Cmd.pack()
    q39Cmd = Button(self, text="Read 0x39", command=self.clickQ39Cmd)
    q39Cmd.pack()
    q3aCmd = Button(self, text="Read 0x3a", command=self.clickQ3aCmd)
    q3aCmd.pack()

  def clickExitCmd(self):
    exit()

  def clickQ38Cmd(self):
    print("clickQ38Cmd")

  def clickQ39Cmd(self):
    print("clickQ39Cmd")

  def clickQ3aCmd(self):
    print("clickQ3aCmd")
