from tkinter import *
from datetime import datetime

number = 0
after_id = " "


def tick():
    global number, after_id
    after_id = root.after(1000, tick)
    f_number = datetime.utcfromtimestamp(number).strftime("%M:%S")

    label_1.configure(text=str(f_number))

    number += 1


def start():
    button_start.grid_forget()
    button_stop.grid(row=1, columnspan=2, sticky="ew")
    tick()


def stop():
    button_stop.grid_forget()
    button_continue.grid(row=1, column=0, sticky="ew")
    button_reset.grid(row=1, column=1, sticky="ew")
    root.after_cancel(after_id)


def continues():
    button_continue.grid_forget()
    button_reset.grid_forget()
    button_stop.grid(row=1, columnspan=2, sticky="ew")
    tick()


def reset():
    global number
    number = 0
    label_1.configure(text="00:00")
    button_reset.grid_forget()
    button_continue.grid_forget()
    button_start.grid(row=1, columnspan=2, sticky="ew")


root = Tk()

root.title("StopWatch")

label_1 = Label(root, width=5, font=("Ubuntu", 100), text="00:00")
label_1.grid(row=0, columnspan=2)

button_start = Button(root, text="Start", font=("Ubuntu", 30), command=start)
button_stop = Button(root, text="Stop", font=("Ubuntu", 30), command=stop)
button_continue = Button(root, text="Continue", font=("Ubuntu", 30), command=continues)
button_reset = Button(root, text="Reset", font=("Ubuntu", 30), command=reset)

button_start.grid(row=1, columnspan=2, sticky="ew")
root.mainloop()
