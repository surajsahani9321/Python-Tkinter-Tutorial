from tkinter import *


def register():
    pass

root=Tk()

namel=Label(root,text="Enter your name : ").grid(row=3,col=0)
usernamel=Label(root,text="Enter your username : ").grid(row=4,col=0)
emaill=Label(root,text="Enter your email : ").grid(row=5,col=0)
passwordl=Label(root,text="Enter your password : ").grid(row=6,col=0)

namee=Label(root).grid(row=3,col=2)
usernamee=Label(root).grid(row=4,col=2)
emaile=Label(root).grid(row=5,col=2)
passworde=Label(root).grid(row=6,col=2)

radio = IntVar()
lbl = Label(text="Gender :")
lbl.grid(row=8,col=0)
R1 = Radiobutton(root, text="MALE", variable=radio, value=1,command=register)
R1.grid(row=8,col=3)
R2 = Radiobutton(root, text="FEMALE", variable=radio, value=2,command=register)
R2.grid(row=8,col=5)


radio2 = IntVar()
lbl = Label(text="Favourite programming language :")
lbl.grid(row=10,col=0)
R3 = Radiobutton(root, text="C", variable=radio2, value=1,command=register)
R3.grid(row=10,col=3)

R4 = Radiobutton(root, text="C++", variable=radio2, value=2,command=register)
R4.grid(row=10,col=5)

R5 = Radiobutton(root, text="Java", variable=radio2, value=3,command=register)
R5.grid(row=10,col=7)

R6 = Radiobutton(root, text="Python", variable=radio2, value=3,command=register)
R6.grid(row=10,col=9)

submit=Button(root,text="Submit").grid(row=12,col=4)