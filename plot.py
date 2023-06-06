from Tkinter import *
from random import randint
from math import *
import math

#globals
items=[]

def grid_lines(canvas):
  for i in canvas.find_all():
    canvas.delete(i)
  canvas.create_line(0,300,800,300)
  canvas.create_line(400,0,400,600)
  
  canvas.create_line(500,298,500,302)
  canvas.create_text(500,310, text="10")
  canvas.create_line(300,298,300,302)
  canvas.create_text(300,310, text="-10 ")
  
  canvas.create_line(410,298,410,302)
  canvas.create_text(410,310, text="1")
  canvas.create_line(390,298,390,302)
  canvas.create_text(390,310, text="-1 ")
  
  
def koniec():
  main.destroy()

def napoveda():
  top=Toplevel()
  lbl=Text(top, font="Courier 12")
  lbl.pack(fill=BOTH)
  for i in dir(math):
    if "_" not in i:
      lbl.insert(END, i+"\n")
  
def append_item(item, c,r, cs=1, rs=1):
  global items
  items.append(item)
  items[-1].grid(column=c, row=r, columnspan=cs, rowspan=rs, sticky="NSEW")
  return items[-1]
  
def evaluate():
  xp,yp=[],[]
  for item in items:
    try:
      item.create_line(0,0,0,0)
      mapa=item
      break
    except:
      pass

  grid_lines(mapa)

  for x in range(-4000,4000):
    x=float(x/10.0)
    try:
      exec(items[3].get())
    except (NameError, SyntaxError):
      mapa.create_text(700,10,text="Bad syntax")
      break
    except ValueError:
      continue
    xp.append(x)
    yp.append(y)

  for i in range(len(xp)-1):
    if abs(xp[i]-xp[i+1])>0.2:
      continue
    mapa.create_line(400+xp[i]*10,300-yp[i]*10,400+xp[i+1]*10,300-yp[i+1]*10)

    
main=Tk()
main.title("Omg")

append_item(Button(main, text="Eval", command=evaluate), 1, 3) #0
append_item(Button(main, text="Exit", command=koniec),2,3) #1
append_item(Canvas(main, height=550, width=800),c=1,r=1, cs=3) #2
grid_lines(items[-1])
append_item(Entry(main), c=1, cs=3, r=2) #3
items[-1].insert(0,"y=log(sin(x))")

append_item(Button(main, text="Commands", command=napoveda),3,3) #4

main.mainloop()
