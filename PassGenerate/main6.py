from tkinter import *
import random


def password(event):
    chars = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    try:
        number = int(entry_how_much.get())
        length = int(entry_length.get())
        for i in range(number):
            tex = ""
            for j in range(length):
                tex += random.choice(chars)

            pas.insert(0, tex)

    except ValueError:
        label1['text'] = "Type correct number"
        label2['text'] = "Type correct length"


root = Tk()
root.title("Random Password Generator")

label1 = Label(root)
label1.grid(row=0, column=2)

label2 = Label(root)
label2.grid(row=1, column=2)

how_much = Label(root, text="How much passwords?")
how_much.grid(row=0, column=0, sticky=E)

entry_how_much = Entry(root)
entry_how_much.grid(row=0, column=1)

length = Label(root, text="Password length")
length.grid(row=1, column=0, sticky=E)

entry_length = Entry(root)
entry_length.grid(row=1, column=1)

button1 = Button(root, text="Submit")
button1.grid(row=2, column=1)

label3 = Label(root, text="Password")
label3.grid(row=3, column=0, sticky=E)
pas = Entry(root)
pas.grid(row=3, column=1)


button1.bind("<Button-1>", password)


root.mainloop()

