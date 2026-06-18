# Student Management System

students = []

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Show Statistics")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll_no = int(input("Enter Roll Number: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        course = input("Enter Course: ")

        student = {
            "roll_no": roll_no,
            "name": name,
            "age": age,
            "course": course
        }

        students.append(student)
        print("Student added successfully!")

    elif choice == "2":
        if not students:
            print("No students found.")
        else:
            print("\nStudent Records:")
            for student in students:
                print(student)

    elif choice == "3":
        roll = int(input("Enter Roll Number to Search: "))

        found = False
        for student in students:
            if student["roll_no"] == roll:
                print("\nStudent Found:")
                print(student)
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "4":
        roll = int(input("Enter Roll Number to Delete: "))

        for student in students:
            if student["roll_no"] == roll:
                students.remove(student)
                print("Student deleted successfully!")
                break
        else:
            print("Student not found.")

    elif choice == "5":

        # List Comprehension
        names = [student["name"] for student in students]
        print("\nStudent Names:", names)

        # Dictionary Comprehension
        student_courses = {
            student["name"]: student["course"]
            for student in students
        }
        print("Student-Course Mapping:", student_courses)

        # Set
        courses = {student["course"] for student in students}
        print("Unique Courses:", courses)

        # Tuple
        total_students = len(students)
        stats = (total_students, len(courses))
        print("Statistics (Total Students, Unique Courses):", stats)

    elif choice == "6":
        print("Thank you for using the Student Management System!")
        break

    else:
        print("Invalid choice! Please try again.")