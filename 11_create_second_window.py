from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("base")


def open_btn():
    global my_img
    top = Toplevel()
    top.title("II")
    my_img = ImageTk.PhotoImage(Image.open("E:\Mine\Python\\first_tk\images\\3.png"))
    Label(top, image=my_img).pack()
    Button(top, text="close window", command=top.destroy).pack()


btn = Button(root, text="Open II", command=open).pack()

root.mainloop()
