from tkinter import *
from tkinter import messagebox
from tkinter.tix import IMAGETEXT
from PIL import ImageTk, Image
fields = ('First Name', 'Last Name', 'Age','Date Of Birth','Contact Number','Username','Email','Password')
def register(entries):
  
   first = str(entries['First Name'].get())
   last = str(entries['Last Name'].get())
   age = str(entries['Age'].get())
   dob = str(entries['Date Of Birth'].get())
   number = str(entries['Contact Number'].get())
   username = str(entries['Username'].get())
   email = str(entries['Email'].get())
   password = str(entries['Password'].get())
   
   surajtxt='First Name : {}\n Last Name : {} \n Age : {}\n Date Of Birth : {}\n Contact Number : {}\n Username : {}\n Email : {}'
  
  
  
  
   print("First Name : %s" % str(first))
   print("First Name : %s" % str(last))
   print("First Name : %s" % str(age))
   print("First Name : %s" % str(dob))
   print("First Name : %s" % str(number))
   print("First Name : %s" % str(username))
   print("First Name : %s" % str(email))
   messagebox.showinfo("Successfull Registration ",surajtxt.format(first,last,age,dob,number,username,email))

def makeform(root, fields):
   entries = {}
   for field in fields:
      row = Frame(root)
     
      lab = Label(row, width=22, text=field+": ", anchor='w')
      ent = Entry(row)
   
      row.pack(side = TOP, fill = X, padx = 5 , pady = 5)
      lab.pack(side = LEFT)
      ent.pack(side = RIGHT, expand = YES, fill = X)
      entries[field] = ent
   return entries
if __name__ == '__main__':
   root = Tk()
   root.title("Registration Form In Tkinter Created By Suraj Sahani")
   root.geometry("500x400")
   ents = makeform(root, fields)

   
   b2 = Button(root, text='SUBMIT',
   command=(lambda e = ents: register(e)))
   b2.pack(side = LEFT, padx = 5, pady = 5)
   b3 = Button(root, text = 'Quit', command = root.quit)
   b3.pack(side = LEFT, padx = 5, pady = 5)
   
   root.mainloop()