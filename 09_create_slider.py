from tkinter import *

root = Tk()
root.title("open file")
root.geometry("300x300")


def slide():
    # Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get())+"x"+str(vertical.get()))


vertical = Scale(root, from_=300, to=0)
vertical.pack()

horizontal = Scale(root, from_=0, to=300, orient=HORIZONTAL)
horizontal.pack()

my_btn = Button(root, text="Click Me!", command=slide).pack()

root.mainloop()
