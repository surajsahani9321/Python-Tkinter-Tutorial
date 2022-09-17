from tkinter import *

top = Tk()

top.geometry("400x250")

lbl = Label(top, text="A list of favourite programming Languages...")

listbox = Listbox(top)

listbox.insert(1, "Java")

listbox.insert(2, "Python")

listbox.insert(3, "C++")

listbox.insert(4, "C")

lbl.pack()
listbox.pack()
btn = Button(top, text="delete", command=lambda listbox1=listbox: listbox1.delete(ANCHOR))
btn.pack()
top.mainloop()
