from tkinter import *


def output(event):
    txt = entry_1.get()

    try:
        if int(txt) < 18:
            label1["text"] = "You still very young"
        elif int(txt) > 90:
            label1["text"] = "You still alive?"
        else:
            label1["text"] = "Welcome!"
    except ValueError:
        label1["text"] = "Enter correct age!"


root = Tk()
root.title("How old are you?")

entry_1 = Entry(root, width=3, font=15)
button_1 = Button(root, text="Verify")
label1 = Label(root, width=27, font=15)

entry_1.grid(row=0, column=0)
button_1.grid(row=0, column=1)
label1.grid(row=0, column=2)

button_1.bind("<Button-1>", output)

root.mainloop()
