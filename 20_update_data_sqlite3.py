from tkinter import *
import sqlite3

root = Tk()
root.title("update1")
root.geometry("600x600")
root.configure(bg="#C16DBB")

# Creat a database or connect to one
conn = sqlite3.connect("MyDB.db")

# Create Cursor
cur = conn.cursor()


# Creat Table - Only Once
# cur.execute('CREATE TABLE students (first_name TEXT, last_name TEXT, course INTEGER, grade REAL)')


def save():
    # Creat a database or connect to one
    conn = sqlite3.connect("MyDB.db")

    # Create Cursor
    cur = conn.cursor()

    record_id = delete_item.get()

    cur.execute("""UPDATE students SET
                first_name = :f_name,
                last_name = :l_name,
                course = :course,
                grade = :grade
                
                WHERE oid = :oid""",
                {'f_name': first_name_editor.get(),
                 'l_name': last_name_editor.get(),
                 'course': course_editor.get(),
                 'grade': grade_editor.get(),
                 "oid": record_id})

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()

    # Close Update Window
    up.destroy()


# Create Update Function
def update():
    global up
    up = Tk()
    up.title("update2")
    up.geometry("600x600")
    up.configure(bg="#C16DBB")

    # Creat a database or connect to one
    conn = sqlite3.connect("MyDB.db")

    # Create Cursor
    cur = conn.cursor()

    # Query the database from the Table
    record_id = delete_item.get()
    cur.execute('SELECT * FROM students WHERE oid ='+record_id)
    # cur.fetchone()
    # cur.fetchmany(10)
    records = cur.fetchall()

    global first_name_editor
    global last_name_editor
    global course_editor
    global grade_editor

    # Create and positioning Entry Boxes
    first_name_editor = Entry(up, width=15, borderwidth=5, fg="#000000", bg="#FB04E0",
                              font=("Times", 16, "italic"), relief=GROOVE)
    first_name_editor.grid(row=0, column=1, pady=(10, 0))

    last_name_editor = Entry(up, width=15, borderwidth=5, fg="#000000", bg="#FB04E0",
                             font=("Times", 16, "italic"), relief=GROOVE)
    last_name_editor.grid(row=1, column=1)

    course_editor = Entry(up, width=15, borderwidth=5, fg="#000000", bg="#FB04E0",
                          font=("Times", 16, "italic"), relief=GROOVE)
    course_editor.grid(row=2, column=1)

    grade_editor = Entry(up, width=15, borderwidth=5, fg="#000000", bg="#FB04E0",
                         font=("Times", 16, "italic"), relief=GROOVE)
    grade_editor.grid(row=3, column=1)

    # Create and positioning Labels
    Label(up, text="First name", bg="#C16DBB", height=1, fg="#000000",
          font=("Times", 16, "italic")).grid(row=0, column=0, padx=5, pady=(10, 0))
    Label(up, text="Last name", bg="#C16DBB", height=1, fg="#000000", font=("Times", 16, "italic")).grid(row=1,
                                                                                                         column=0)
    Label(up, text="Course", bg="#C16DBB", height=1, fg="#000000", font=("Times", 16, "italic")).grid(row=2, column=0)
    Label(up, text="Grade", bg="#C16DBB", height=1, fg="#000000", font=("Times", 16, "italic")).grid(row=3, column=0)

    # Loop Thru Results
    for rec in records:
        first_name_editor.insert(0, rec[0])
        last_name_editor.insert(0, rec[1])
        course_editor.insert(0, rec[2])
        grade_editor.insert(0, rec[3])

    # Create Save Button
    Button(up, text="Save Student", command=save, fg="#D09CF7", bg="#690AAD",
           activebackground="#D09CF7", activeforeground="#690AAD",
           font=("Times", 16, "italic"), relief=GROOVE).grid(row=5, column=0, columnspan=2, padx=5, pady=(10, 0),
                                                             ipadx=85)

    # # Creat a database or connect to one
    # conn = sqlite3.connect("MyDB.db")

    # # Create Cursor
    # cur = conn.cursor()
    #
    # # Delete record
    # cur.execute()
    #
    # # Commit changes
    # conn.commit()
    #
    # # Close connection
    # conn.close()


# Create Delete Function
def delete():
    # Creat a database or connect to one
    conn = sqlite3.connect("MyDB.db")

    # Create Cursor
    cur = conn.cursor()

    # Delete record
    cur.execute('DELETE FROM students WHERE oid='+delete_item.get())

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()


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
        print_records += '#'+str(rec[4])+' '+str(rec[0])+' '+str(rec[1])+' / '+str(rec[2])+' / '+str(rec[3])+'\n'

    # Create and positioning Label for the Result
    Label(root, text=print_records, bg="#C16DBB", fg="#000000",
          font=("Times", 14, "italic"), justify=LEFT).grid(row=9, column=0, columnspan=2, pady=(5, 0))

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()


# Create and positioning Entry Boxes
first_name = Entry(root, width=15, borderwidth=5, fg="#000000", bg="#FB04E0",
                   font=("Times", 16, "italic"), relief=GROOVE)
first_name.grid(row=0, column=1, pady=(10, 0))

last_name = Entry(root, width=15, borderwidth=5, fg="#000000", bg="#FB04E0",
                  font=("Times", 16, "italic"), relief=GROOVE)
last_name.grid(row=1, column=1)

course = Entry(root, width=15, borderwidth=5, fg="#000000", bg="#FB04E0",
               font=("Times", 16, "italic"), relief=GROOVE)
course.grid(row=2, column=1)

grade = Entry(root, width=15, borderwidth=5, fg="#000000", bg="#FB04E0",
              font=("Times", 16, "italic"), relief=GROOVE)
grade.grid(row=3, column=1)

delete_item = Entry(root, width=15, borderwidth=5, fg="#000000", bg="#FB04E0",
                    font=("Times", 16, "italic"), relief=GROOVE)
delete_item.grid(row=4, column=1)

# Create and positioning Labels
Label(root, text="First name", bg="#C16DBB", height=1, fg="#000000",
      font=("Times", 16, "italic")).grid(row=0, column=0, padx=5, pady=(10, 0))
Label(root, text="Last name", bg="#C16DBB", height=1, fg="#000000", font=("Times", 16, "italic")).grid(row=1, column=0)
Label(root, text="Course", bg="#C16DBB", height=1, fg="#000000", font=("Times", 16, "italic")).grid(row=2, column=0)
Label(root, text="Grade", bg="#C16DBB", height=1, fg="#000000", font=("Times", 16, "italic")).grid(row=3, column=0)
Label(root, text="Del ID #", bg="#C16DBB", height=1, fg="#000000", font=("Times", 16, "italic")).grid(row=4, column=0)

# Create and positioning Submit Button
Button(root, text="Add Student", command=submit, fg="#D09CF7", bg="#690AAD",
       activebackground="#D09CF7", activeforeground="#690AAD",
       font=("Times", 16, "italic"), relief=GROOVE).grid(row=5, column=0, columnspan=2, padx=5, pady=(10, 0), ipadx=85)

# Create and positioning Query Button
Button(root, text="Show Students", command=query, fg="#D09CF7", bg="#690AAD",
       activebackground="#D09CF7", activeforeground="#690AAD",
       font=("Times", 16, "italic"), relief=GROOVE).grid(row=6, column=0, columnspan=2, padx=5, pady=(10, 0), ipadx=75)

# Create and positioning Delete Button
Button(root, text="Delete Student", command=delete, fg="#D09CF7", bg="#690AAD",
       activebackground="#D09CF7", activeforeground="#690AAD",
       font=("Times", 16, "italic"), relief=GROOVE).grid(row=7, column=0, columnspan=2, padx=5, pady=(10, 0), ipadx=78)

# Create and positioning Update Button
Button(root, text="Update Student", command=update, fg="#D09CF7", bg="#690AAD",
       activebackground="#D09CF7", activeforeground="#690AAD",
       font=("Times", 16, "italic"), relief=GROOVE).grid(row=8, column=0, columnspan=2, padx=5, pady=(10, 0), ipadx=74)

# Commit changes
conn.commit()

# Close connection
conn.close()

root.mainloop()
