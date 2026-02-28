from tkinter import *

root = Tk()
root.geometry("644x900")
scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvariable=scvalue, font="lucida 40 bold")
screen.pack()

root.mainloop()