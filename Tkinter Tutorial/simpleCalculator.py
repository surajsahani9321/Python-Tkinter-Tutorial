import tkinter as tk
from functools import partial


def call_result(label_result1,label_result2,label_result3,label_result4, n1, n2):
    num1 = (n1.get())
    num2 = (n2.get())
    add = int(num1) + int(num2)
    sub = int(num1) - int(num2)
    mul = int(num1) * int(num2)
    div = int(num1) / int(num2)
    label_result1.config(text="Addition = %d" % add)
    label_result2.config(text="Substraction = %d" % sub)
    label_result3.config(text="Multiplication = %d" % mul)
    label_result4.config(text="Division = %d" % div)
    return


root = tk.Tk()
root.geometry('400x200+100+200')

root.title('Calculator')

number1 = tk.StringVar()
number2 = tk.StringVar()

labelNum1 = tk.Label(root, text="Number 1 :-").grid(row=1, column=1)

labelNum2 = tk.Label(root, text="Number 2:-").grid(row=2, column=1)

labelResult1 = tk.Label(root)
labelResult1.grid(row=7, column=2)

labelResult2 = tk.Label(root)
labelResult2.grid(row=8, column=2)

labelResult3 = tk.Label(root)
labelResult3.grid(row=9, column=2)

labelResult4 = tk.Label(root)
labelResult4.grid(row=10, column=2)

entryNum1 = tk.Entry(root, textvariable=number1).grid(row=1, column=2)

entryNum2 = tk.Entry(root, textvariable=number2).grid(row=2, column=2)

call_result = partial(call_result, labelResult1,labelResult2,labelResult3,labelResult4, number1, number2)

buttonCal = tk.Button(root, text="Calculate", command=call_result,bg="yellow").grid(row=3, column=2)

root.mainloop()