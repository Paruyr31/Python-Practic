from tkinter import *
import random


def password():
    pass


root = Tk()
root.title("Test")

button1 = Button(root, text="Type")
button1.grid(row=0, column=1)

label1 = Label(root, width=27, font=15)
label1.grid(row=0, column=2)

button1.bind("<Button-1>", password)

root.mainloop()

for i in range(48, 123):
    a = ""
    a += chr(i)
    print(type(a))