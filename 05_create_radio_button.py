from tkinter import *

root = Tk()
root.title("radioButtons")

MODES = [
    ("Pepperoni", "Pepperoni"),
    ("FourSeasons", "FourSeasons"),
    ("AliBaba", "AliBaba"),
    ("Mozzarella", "Mozzarella"),
    ("Devil", "Devil")
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)


def click(value):
    my_label = Label(root, text=value)
    my_label.pack()


# Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: click(r.get())).pack()
# Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: click(r.get())).pack()
#
# my_label = Label(root, text=r.get())
# my_label.pack()

my_button = Button(root, text="Click me!", command=lambda: click(pizza.get()))
my_button.pack()

root.mainloop()

len(adsdf)


len