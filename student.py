class Student:
    def __init__(self,roll,name,subjects):
        self.roll = roll
        self.name = name
        self.subjects = subjects
        self.total_marks = self.calculate_total()
        self.grade = self.calculate_grade()

    def calculate_total(self):
            return sum(self.subjects.values())
        

    def calculate_grade(self):
            marks = self.total_marks
            if marks >= 450:
                return "A+"
            elif marks >= 375:
                return "A"
            elif marks >= 300:
                return "B"
            elif marks >= 175:
                return "C"
            else:
                return "Fail"
            

       # Convert the object to dictionary

    def convert_to_dict(self):
     return {
        "Roll No":self.roll,
        "Name": self.name,
        "Subjects": self.subjects,
        "Total marks": self.total_marks,
        "Grade": self.grade
    }