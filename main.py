#initialising dictionary
student_grades = {}

#add a new student
def Add_student(name,grade):
    student_grades[name] = grade
    #[sagar] = 100
    print(f"added {name} with a {student_grades}")
    #added sagar with a 100

#update a student
def Update_student(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        #sagarn=200
        print(f"{name} with marks are updated {grade}")

    else:
        print(f"{name} is not found!")

#delete a student
def Delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} has been successfully deleted")

    else:
        print(f"{name} is not found!")

#view all student
def Display_all_student():
    if student_grades:
        for name, grade in student_grades.items():
         print(f"{name}: {grade}")

    else:
        print("no students found/added")

def main():
    while True:
        print('\n student grades management system')
        print("1.add student")
        print("2. update student")
        print("3. delete student")
        print("4. view student")
        print("5. exit")

        choice = int(input("enter your choice = "))
        if choice == 1:
            name = input("enter student name = ")
            grade = int(input("enter student grade = "))
            Add_student(name,grade)

        elif choice == 2:
            name = input("enter student name = ")
            grade = int(input("enter student grade = "))
            Update_student(name,grade)

        elif choice ==3:
            name = input("enter student name = ")
            Delete_student(name)

        elif choice ==4:
            Display_all_student()

        elif choice ==5:
            print("closing the program")
            break
        else:
            print("invalid choice")

main()
    

    




