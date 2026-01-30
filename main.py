from operations import StudentManager

manager = StudentManager()

while True:
    print()
    print()
    print()
    print()
    print("WELCOME TO STUDENT MANAGMEMENT SYSTEM")
    print()
    print("Which task you want to do")
    print()
    print("Here are the choices")
    print()
    print("""
1. Add Student
2. Search Student
3. Update Student
4. Delete Student
5. Exit
""")
    
    choice = int(input("Enter your choice (1-5): "))

    if choice == 1:
        manager.add_student()
    elif choice == 2:
        manager.search_student_by_rollno()
    elif choice == 3:
         manager.update_student()
    elif choice == 4:
        manager.delete_student()
    elif choice == 5:
        print()
        print("Thank you!")
        print()
        break
    else:
        print()
        print("❌ Invalid choice")