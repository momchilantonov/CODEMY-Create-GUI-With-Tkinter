from tkinter import *
import sqlite3

root = Tk()
root.title("open file")
root.geometry("600x300")

# Creat a database or connect to one
conn = sqlite3.connect("MyDB.db")

# Create Cursor
cur = conn.cursor()


# Creat Table - Only Once
# cur.execute('CREATE TABLE students (first_name TEXT, last_name TEXT, course INTEGER, grade REAL)')


# Create Submit function
def submit():
    # Creat a database or connect to one
    conn = sqlite3.connect("MyDB.db")

    # Create Cursor
    cur = conn.cursor()

    # Insert Into Table
    cur.execute('INSERT INTO students VALUES (:f_name, :l_name, :course, :grade)',
                {'f_name': first_name.get(), 'l_name': last_name.get(), 'course': course.get(), 'grade': grade.get()})

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()

    # Clear Text Boxes
    first_name.delete(0, END)
    last_name.delete(0, END)
    course.delete(0, END)
    grade.delete(0, END)


# Create Query function
def query():
    # Creat a database or connect to one
    conn = sqlite3.connect("MyDB.db")

    # Create Cursor
    cur = conn.cursor()

    # Query the database from the Table
    cur.execute('SELECT *, oid FROM students')
    # cur.fetchone()
    # cur.fetchmany(10)
    records = cur.fetchall()

    # Loop Thru Results
    print_records = ""
    for rec in records:
        print_records += str(rec[0])+' '+str(rec[1])+' '+str(rec[2])+' '+str(rec[3])+"\n"

    # Create and positioning Label for the Result
    Label(root, text=print_records).grid(row=7, column=0, columnspan=3)

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()


# Create and positioning Entry Boxes
first_name = Entry(root, width=15)
first_name.grid(row=1, column=1, padx=20, sticky=W)
last_name = Entry(root, width=15)
last_name.grid(row=2, column=1, padx=20, sticky=W)
course = Entry(root, width=5)
course.grid(row=3, column=1, padx=20, sticky=W)
grade = Entry(root, width=5)
grade.grid(row=4, column=1, padx=20, sticky=W)

# Create and positioning Labels
Label(root, text="First Name").grid(row=1, column=0, sticky=E)
Label(root, text="Last Name").grid(row=2, column=0, sticky=E)
Label(root, text="Course").grid(row=3, column=0, sticky=E)
Label(root, text="Grade").grid(row=4, column=0, sticky=E)

# Create and positioning Submit Button
Button(root, text="Add Record", command=submit).grid(row=5, column=1, columnspan=2, padx=20, pady=10, ipadx=15,
                                                     sticky=E)

# Create a Query Button
Button(root, text="Show Records", command=query).grid(row=6, column=1, columnspan=2, padx=20, pady=10, ipadx=10,
                                                      sticky=E)

# Commit changes
conn.commit()

# Close connection
conn.close()

root.mainloop()
