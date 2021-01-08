from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("messageBoxes")


def popup():
    # messagebox.showinfo("This is my Popup!", "Hello World!")
    # messagebox.showwarning("This is my Popup!", "Hello World!")
    # messagebox.showerror("This is my Popup!", "Hello World!")
    # messagebox.askquestion("This is my Popup!", "Hello World!")
    # messagebox.askokcancel("This is my Popup!", "Hello World!")
    response = messagebox.askyesno("This is my Popup!", "Hello World!")
    # Label(root, text=response).pack()
    if response == 1:
        Label(root, text="Yes!").pack()
    else:
        Label(root, text="No!").pack()


Button(root, text="Popup", command=popup).pack()

root.mainloop()
