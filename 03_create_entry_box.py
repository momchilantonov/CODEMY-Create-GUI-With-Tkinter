from tkinter import *

root = Tk()

entry = Entry(root, width=20, borderwidth=5, fg="blue", bg="white")
entry.pack()
entry.insert(0, "Enter your name")


def my_click():
    my_label1 = Label(root, text="Hello "+entry.get())
    my_label1.pack()


my_button = Button(root, text="Enter your name", command=my_click, fg="white", bg="black")
my_button.pack()

root.mainloop()
