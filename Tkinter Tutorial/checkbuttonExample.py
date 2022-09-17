from tkinter import *

top=Tk()

top.geometry("300x300")

check1=IntVar()
check2=IntVar()
check3=IntVar()

c1=Checkbutton(top,text="Python",onvalue=1,offvalue=0,height=2,width=4,variable=check1)
c2=Checkbutton(top,text="Java",onvalue=1,offvalue=0,height=2,width=4,variable=check2)
c3=Checkbutton(top,text="C++",onvalue=1,offvalue=0,height=2,width=4,variable=check3)

c1.pack()
c2.pack()
c3.pack()

top=mainloop()