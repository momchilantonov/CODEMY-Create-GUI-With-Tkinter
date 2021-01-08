from tkinter import *


root = Tk()
root.title("open file")
root.geometry("300x300")


def show():
    Label(root, text=var.get()).pack()


var = StringVar()
# var = IntVar()

c = Checkbutton(root, text="Check it!", variable=var, onvalue="On", offvalue="Off")
c.deselect()
c.pack()

Button(root, text="Show me", command=show).pack()

root.mainloop()
