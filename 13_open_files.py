from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk()
root.title("open file")


def open_btn():
    global my_img
    root.filename = filedialog.askopenfilename(initialdir="\\first_tk\images", title="Select a file",
                                               filetypes=(("png files", "*.png"), ("all files", "*.*")))
    Label(root, text=root.filename).pack()
    my_img = ImageTk.PhotoImage(Image.open(root.filename))
    Label(image=my_img).pack()


my_btn = Button(root, text="Open file", command=open_btn).pack()

root.mainloop()
