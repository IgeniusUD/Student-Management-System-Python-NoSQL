import stud_tkdb as studb

import tkinter as tk

mainWindow = tk.Tk()
mainWindow.title("Student Database Management System")

heading_label = tk.Label(mainWindow, text ="Student Database Management")
heading_label.pack()

label1=tk.Label(mainWindow, text="Enter Name")
label1.pack()
entry1 = tk.Entry(mainWindow)
entry1.pack()

label2=tk.Label(mainWindow, text="Enter Course")
label2.pack()
entry2 = tk.Entry(mainWindow)
entry2.pack()

label3=tk.Label(mainWindow, text="Enter Address")
label3.pack()
entry3 = tk.Entry(mainWindow)
entry3.pack()

def write_data():
    name = entry1.get()
    course = entry2.get()
    address = entry3.get()
    studb.insert(name,course,address)


def read_data():
    students_record=studb.show()
    for student in students_record.each():
        record = student.val()
        print("Student name is: ", record['name'])
        print("Student course is: ", record['course'])
        print("Student address is: ", record['address'])

write_button = tk.Button(mainWindow, text="Write Data",command=lambda : write_data())
write_button.pack()

read_button = tk.Button(mainWindow, text="Read Data",command=lambda : read_data())
read_button.pack()

mainWindow.mainloop()