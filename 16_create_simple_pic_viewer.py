from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("viewer")

my_img1 = ImageTk.PhotoImage(Image.open("E:\Mine\Python\\first_tk\images\\1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("E:\Mine\Python\\first_tk\images\\2.png"))
my_img3 = ImageTk.PhotoImage(Image.open("E:\Mine\Python\\first_tk\images\\3.png"))
my_img4 = ImageTk.PhotoImage(Image.open("E:\Mine\Python\\first_tk\images\\4.jpg"))

image_list = [my_img1, my_img2, my_img3, my_img4]

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)


def bwd(image_num):
    global my_label
    global button_fwd
    global button_bwd

    my_label.grid_forget()
    my_label = Label(image=image_list[image_num-1])
    button_fwd = Button(root, text="->", command=lambda: fwd(image_num+1))
    button_bwd = Button(root, text="<-", command=lambda: bwd(image_num-1))

    if image_num == 1:
        button_bwd = Button(root, text="<-", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_bwd.grid(row=1, column=0)
    button_fwd.grid(row=1, column=2)


def fwd(image_num):
    global my_label
    global button_fwd
    global button_bwd

    my_label.grid_forget()
    my_label = Label(image=image_list[image_num-1])
    button_fwd = Button(root, text="->", command=lambda: fwd(image_num+1))
    button_bwd = Button(root, text="<-", command=lambda: bwd(image_num-1))

    if image_num == 4:
        button_fwd = Button(root, text="->", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_bwd.grid(row=1, column=0)
    button_fwd.grid(row=1, column=2)


button_bwd = Button(root, text="<-", command=bwd, state=DISABLED)
button_exit = Button(root, text="Exit Program", command=root.quit)
button_fwd = Button(root, text="->", command=lambda: fwd(2))

button_bwd.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_fwd.grid(row=1, column=2)

root.mainloop()
