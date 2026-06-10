# Mini Project: Student Record Management System (SRMS)

student=[]

def add_students():
    name=input("Enter student name: ")
    student_id=input("Enter student ID: ")
    student_dept=input("Enter student department: ")
    student.append({"name":name,"id":student_id,"dept":student_dept})
    print("Student added successfully!")

def view_students():
    if not student:
        print("No student records found.")
    else:
        for s in student:
            print(f"Name: {s['name']}, ID: {s['id']}, Department: {s['dept']}")

def search_student():
    search_id=input("Enter student ID to search: ")
    for s in student:
        if s['id'] == search_id:
            print(f"Name: {s['name']}, ID: {s['id']}, Department: {s['dept']}")
            return
        print("Student not found.")

def exit():
    print("Exiting the program. Goodbye!")
    quit()

def main():
    while True:
        print("\nStudent Record Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Exit")

        choice=int(input("Enter your choice: "))
        if choice==1:
            add_students()
        elif choice==2:
            view_students()
        elif choice==3:
            search_student()
        elif choice==4:
            exit()
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()