from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("images")
root.iconbitmap("E:\Mine\Python\\first_tk\logo_ce7_icon.ico")

my_img = ImageTk.PhotoImage(Image.open("E:\Mine\Python\\first_tk\LOGO.jpg"))
my_label = Label(image=my_img)
my_label.pack()

button_quit = Button(root, text="EXIT", command=root.quit)
button_quit.pack()

root.mainloop()
