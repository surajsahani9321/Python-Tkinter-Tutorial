from tkinter import *

parent=Tk()

# redbutton=Button(parent,text="Red",fg="red")
# redbutton.pack(side=LEFT)
# greenbutton = Button(parent, text = "Black", fg = "green")
# greenbutton.pack( side = RIGHT )
# bluebutton = Button(parent, text = "Blue", fg = "blue")
# bluebutton.pack( side = TOP )
# blackbutton = Button(parent, text = "Green", fg = "black")
# blackbutton.pack( side = BOTTOM)


name = Label(parent,text = "Name").grid(row = 0, column = 0)
e1 = Entry(parent).grid(row = 0, column = 1)
password = Label(parent,text = "Password").grid(row = 1, column = 0)
e2 = Entry(parent).grid(row = 1, column = 1)
submit = Button(parent, text = "Submit").grid(row = 4, column = 0)

parent=mainloop()