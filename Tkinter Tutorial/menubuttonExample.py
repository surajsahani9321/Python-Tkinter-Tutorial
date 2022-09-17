from tkinter import *

top=Tk()

top.geometry("500x500")

mb=Menubutton(top,text="Programming Languages",relief=FLAT)
# mb.grid()
mb.m=Menu(mb)
mb["m"]=mb.m
mb.m.add_checkbutton(label="Java",variable=IntVar)
mb.m.add_checkbutton(label="Python",variable=IntVar)
mb.m.add_checkbutton(label="C++",variable=IntVar)
mb.m.add_checkbutton(label="C",variable=IntVar)

mb.pack()
top=mainloop()