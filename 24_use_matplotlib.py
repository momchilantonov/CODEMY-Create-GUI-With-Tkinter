from tkinter import *
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.title("weather")
root.geometry("400x200")


def graph():
    house_prices = np.random.normal(200000, 25000, 5000)
    plt.hist(house_prices, 300)
    plt.show()


my_btn = Button(root, text="Graph It!", command=graph)
my_btn.pack()

root.mainloop()
