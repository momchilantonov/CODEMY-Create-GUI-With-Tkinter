from tkinter import *


root = Tk()
root.title("frame")

frame = LabelFrame(root, text="This is my frame ....", padx=50, pady=50)
frame.pack(padx=10, pady=10)

b = Button(frame, text="Dont't Click Here!")
b.pack()

root.mainloop()
