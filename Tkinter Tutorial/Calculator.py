from tkinter import *


def add():
    a = int(e1.get())
    b = int(e2.get())
    leftdata = str(a + b)
    left.insert(1, leftdata)
    
def sub():
    a = int(e1.get())
    b = int(e2.get())
    leftdata = str(a - b)
    left.insert(1, leftdata)

def mul():
    a = int(e1.get())
    b = int(e2.get())
    leftdata = str(a * b)
    left.insert(1, leftdata)
def div():
    a = int(e1.get())
    b = int(e2.get())
    leftdata = str(a / b)
    left.insert(1, leftdata)


w1 = PanedWindow()
w1.pack(fill=BOTH, expand=1)

left = Entry(w1, bd=5)
w1.add(left)

w2 = PanedWindow(w1, orient=VERTICAL)
e1 = Entry(w2)
e2 = Entry(w2)
b1 = Button(w2, text="Add", command=add)
b2 = Button(w2, text="Sub", command=sub)
b3 = Button(w2, text="Mul", command=mul)
b4 = Button(w2, text="Div", command=div)
w2.add(e1)
w2.add(e2)
w2.add(b1)
w2.add(b2)
w2.add(b3)
w2.add(b4)
w1.add(w2)

mainloop()