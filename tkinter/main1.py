from tkinter import *


def left_click(event):
    frame1.configure(bg="red")
    frame2.configure(bg="white")
    frame3.configure(bg="white")


def middle_click(event):
    frame1.configure(bg="white")
    frame2.configure(bg="red")
    frame3.configure(bg="white")


def right_click(event):
    frame1.configure(bg="white")
    frame2.configure(bg="white")
    frame3.configure(bg="red")


root = Tk()
root.configure(bg="black")

frame1 = Frame(root, width=250, heigh=250, bg='white')
frame2 = Frame(root, width=250, heigh=250, bg='white')
frame3 = Frame(root, width=250, heigh=250, bg='white')

frame1.grid(row=0, column=0)
frame2.grid(row=0, column=1, padx=1)
frame3.grid(row=0, column=2)

root.bind("<Button-1>", left_click)
root.bind("<Button-2>", middle_click)
root.bind("<Button-3>", right_click)

root.mainloop()