# -*- coding: cp1250 -*-
from Tkinter import *
from random import randint
from numpy import *
import numpy as np
import matplotlib.pyplot as plt
import sys

#globals
items=[]

def koniec():
  main.destroy()

def throw(case,text):
  top=Toplevel()
  top.title(str(case))
  lbl=Label(top, text=str(text)).pack()
  Button(top, text="OK", command=top.destroy).pack(fill=BOTH)

def napoveda():
  top=Toplevel()
  lbl=Text(top, font="Courier 12")
  lbl.pack(fill=BOTH)
  for i in dir(np):
    if "_" not in i:
      lbl.insert(END, i+"\n")
  
def append_item(item, c,r, cs=1, rs=1):
  global items
  items.append(item)
  items[-1].grid(column=c, row=r, columnspan=cs, rowspan=rs, sticky="NSEW")
  return items[-1]
  
def evaluate(key=0):
  try:
    data=items[-1].get().split(";")
    x=np.arange(eval(data[1].split("<")[1].split(",")[0]),
                eval(data[1].split(",")[1][:-1])+eval(data[2].split("=")[1]),
                eval(data[2].split("=")[1])) #rozlisenie
    exec(data[0])
    plt.plot(x,y)
    plt.show()
  except NameError:
    throw(sys.exc_info()[0], f"{str(sys.exc_info()[1])}, hint: check variables.")
  except SyntaxError:
    throw(sys.exc_info()[0], f"{str(sys.exc_info()[1])}, hint: check brackets.")
  except ValueError:
    pass
   
    
main=Tk()
main.title("Plot Out")

append_item(Button(main, text="Plot", command=evaluate), 1, 3) #0
append_item(Button(main, text="Exit", command=koniec),3,3) #1
append_item(Button(main, text="Commands", command=napoveda),2,3) #2
append_item(Entry(main, width=50, font="COURIER 14"), c=1, cs=3, r=2) #3
items[-1].insert(0,u"y=sin(x); x<-2*pi, 2*pi>; step=0.1")

main.bind("<Return>", evaluate)

main.mainloop()
