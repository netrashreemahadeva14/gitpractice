students = []

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        name = input("Enter student name: ")
        roll_no = input("Enter roll number: ")
        students.append({"name": name, "roll_no": roll_no})
        print("Student added successfully!")

    elif choice == "2":
        if not students:
            print("No students in the database.")
        else:
            print("\nStudent List:")
            for i, student in enumerate(students, start=1):
                print(f"{i}. Name: {student['name']}, Roll No: {student['roll_no']}")

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")