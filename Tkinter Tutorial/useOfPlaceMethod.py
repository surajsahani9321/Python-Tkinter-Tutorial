from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry("400x250")

def register():
    messagebox.showinfo("Hello", "Submit Button is clicked ")

name = Label(top, text = "User Name").place(x = 30,y = 50)
email = Label(top, text = "Email").place(x = 30, y = 90)
password = Label(top, text = "Password").place(x = 30, y = 130)
confirmpassword = Label(top, text = "Confirm Password").place(x = 30, y = 170)
e1 = Entry(top).place(x = 150, y = 50)
e2 = Entry(top).place(x = 150, y = 90)
e3 = Entry(top).place(x = 150, y = 130)
e4 = Entry(top).place(x = 150, y = 170)
submit=Button(top,text="Submit",fg="green",command=register).place(x=80,y=210)
# submit.pack(side=BOTTOM)
top.mainloop()
