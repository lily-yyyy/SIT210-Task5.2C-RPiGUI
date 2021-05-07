from tkinter import *
import RPi.GPIO as GPIO

import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)

def red():
   GPIO.output(22,GPIO.HIGH)
   GPIO.output(16,GPIO.LOW)
   GPIO.output(8,GPIO.LOW)

def yellow():
   GPIO.output(22,GPIO.HIGH)
   GPIO.output(5,GPIO.LOW)
   GPIO.output(8,GPIO.LOW)
   
def green():
   GPIO.output(8,GPIO.HIGH)
   GPIO.output(16,GPIO.LOW)
   GPIO.output(22,GPIO.LOW)

root = Tk()
var = IntVar()
R1 = Radiobutton(root, text="RED", variable=var, value=1,
                  command=green)
R1.pack( anchor = W )

R2 = Radiobutton(root, text="YELOW", variable=var, value=2,
                  command=blue)
R2.pack( anchor = W )

R3 = Radiobutton(root, text="GREEN", variable=var, value=3,
                  command=yellow)
R3.pack( anchor = W)

label = Label(root)
label.pack()
root.mainloop()
