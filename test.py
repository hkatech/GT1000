import tkinter as tk
from tkinter import *

class Window(Frame):
  def __init__(self, master=None):
    Frame.__init__(self,master)
    self.master = master

    self.pack(fill=BOTH, expand=1)

    # Try a button
    exitCmd =  Button(self, text="Exit", command=self.clickExitCmd)
    exitCmd.place(x=0,y=0)

    # Create a label
    label = tk.Label(root, text="Hello World!")


    # Lay out label
    label.pack()


  def clickExitCmd(self):
    exit()

# Create the main window
root = tk.Tk()
app = Window(root)
root.title("My GUI")
#root.geometry("320x200")
root.geometry("800x480")


# Run forever!
root.mainloop()

