from tkinter import *
import sqlite3
from tkinter import filedialog
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("open file")
root.geometry("300x300")


# Creat a database or connect to one
conn = sqlite3.connect("MyDB.db")


# Create cursor
cur = conn.cursor()

# Creat Table
cur.execute("CREATE TABLE students(id INT primary key, first_name TEXT, last_name TEXT, grade REAL)")

# # Commit changes
conn.commit()

# Close connection
conn.close()


root.mainloop()
