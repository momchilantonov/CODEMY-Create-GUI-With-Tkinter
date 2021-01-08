from tkinter import *

root = Tk()
root.title("open file")
root.geometry("300x300")


def show():
    Label(root, text=clicked.get()).pack()


options = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options)
drop.pack()

btn = Button(root, text="Choose", command=show)
btn.pack()

root.mainloop()
