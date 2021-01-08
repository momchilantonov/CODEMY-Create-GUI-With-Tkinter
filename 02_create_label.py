from tkinter import *

root = Tk()

# my_label1 = Label(root, text="hello").grid(row=0, column=0)
# my_label2 = Label(root, text="my name is ...").grid(row=1, column=0)
# my_label3 = Label(root, text="My hobby is ...").grid(row=1, column=1)

my_label1 = Label(root, text="Hello")
my_label2 = Label(root, text="My name is ...")
my_label3 = Label(root, text="My hobby is ...")

my_label1.grid(row=0, column=0)
my_label2.grid(row=1, column=0)
my_label3.grid(row=1, column=1)

root.mainloop()
