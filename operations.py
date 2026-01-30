import json 
import os
from student import Student

FILE_NAME = 'studentsoop.json'

class StudentManager:
    def __init__(self):
        self.students = []
        self.load_students()


    def load_students(self):
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "r") as file:
                data = json.load(file)

                for s in data:
                    student = Student(
                        s["Roll No"],
                        s["Name"],
                        s["Subjects"]
                    )

                    self.students.append(student)


    def save_students(self):
        with open(FILE_NAME, "w") as file:
            json.dump(
                [s.convert_to_dict() for s in self.students],
                 file,
                 indent = 4
            )



    def add_student(self):
        print()
        print("Enter the details of new Student :->")
        print()
        roll = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        print("Enter marks for each Subject :->")

        # creating one more dict.......... and add it to in students
        subjects = {
            "IP": int(input("Enter IP marks: ")),
            "Chemistry": int(input("Enter Chemistry Marks: ")),
            "Maths": int(input("Enter Maths marks: ")),
            "English": int(input("Enter English marks: ")),
            "Q & LA": int(input("Enter Q & LA marks: "))
        }
        
   # func...  to check that marks are only out of 100 
        for marks in subjects.values():
            if marks < 0 or marks > 100:
                print()
                print("Marks are only out of 100")
                return   

        student = Student(roll,name,subjects)
        self.students.append(student)

        print()
        print("✅ Details added successfully!")
        print()
        print("Details of New Student  :->")
        print()
        print("Roll No     : ",student.roll)
        print("Name        :", student.name)
        print("Subjects     :->")
        for subject,marks in student.subjects.items():
           print(f"{subject:<12}:", marks)
        print("Total Marks :", student.total_marks)
        print("Grade       :", student.grade)      
        

        self.save_students()

    #  searching a student detail  in list
    def search_student_by_rollno(self):
        print()
        roll = int(input("Enter the roll number of student which you want to search: "))
    
        for s in self.students:
          if s.roll == roll:
             print()
             print("✅ Student Found")
             print()
             self.display_student(s)
             return
        print()
        print("❌ Roll No not exist")





    def update_student(self):
        print()
        roll = int(input("Enter the Roll No of student which you want to update: "))
    
        
        # loop to check that roll no exist in list
        for s in self.students:
          if s.roll == roll:
             
              print()
              print("What details are you want to update :->")
              print()
              print("Here are the choices")
              print()
              print("1. Update Student Roll No")
              print("2. Update Student Name")
              print("3. Update Student marks")
              print()
              choice = int(input("Enter your choice (1-3): "))

              # update roll no
              if choice ==1:
               print()
               s.roll = int(input("Enter new roll no of student: "))
                
               print()
               print("✅ Roll No Updated")
               print()



             # update name
              elif choice ==2:
               print()
               s.name = input("Enter new name of student:  ")
              
               print()
               print("✅ Name updated") 
               print()
             

              # update subject marks
              elif choice ==3:
                print()
               
                print("CHOOSE SUBJECT :->")
                print()
                subject = input("Enter subject name: ")
                print()

                if subject in s.subjects:
                   s.subjects[subject] = int(input("Enter new marks of subject: "))
                   s.total_marks = s.calculate_total()
                   s.grade = s.calculate_grade()
              else:
                print()
                print("❌ Invalid choice")  

              self.save_students()
              print()
              print("✅ Student details Updated")
              return
        print()
        print("❌ Roll No not exist")   


    

    def delete_student(self):
       print()
       roll = int(input("Enter the roll no of student which you want to delete detail: "))
       for s in self.students:
          if s.roll == roll:
             self.students.remove(s)
             self.save_students()
             print()
             print("✅ Student details deleted successfully")
             return
       print()
       print("❌ Roll No not exist") 



    def display_student(self,s):
       print()
       print("Roll No     :",s.roll)       
       print("Name        :",s.name)
       print("Subjects    :->")
       for sub,marks in s.subjects.items():
          print(f"{sub:<12}:", marks)
       print("Total Marks :", s.total_marks)
       print("Grade       :", s.grade)

     