import pyrebase

## add your own configuration for firebase.
config = {
    "apiKey" : "AIzaSyBWFBb-EhtFQVESZ7mxiAi7p-A1H8zosy0",
    "authDomain": "pythondemo-3780b.firebaseapp.com",
    "databaseURL": "https://pythondemo-3780b.firebaseio.com",
    "storageBucket": "pythondemo-3780b.appspot.com",
}

connection = pyrebase.initialize_app(config)

## reading data from firebase
firebase = connection.database()


##insert records to the database using insert function
def insert(name,course,address):
    new_student_record = {
        'name': name,
        'course': course,
        'address': address
    }
    firebase.child("StudentManage").child("Students").push(data=new_student_record)
    print("New value inserted successfully.")

##show all the records stored in database
def show():
    students_record = firebase.child("StudentManage").child("Students").get()
    return  students_record;