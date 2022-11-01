"""
TASK 2
Write a base class to represent a student. Below is a starter code.
Feel free to add any more new features to your class.
As a minimum a student has a name and age and a unique ID.
Create a new subclass from student to represent a concrete student doing a specialization, for example:
Software Student and Data Science student.
"""
class Student:

    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.subjects = dict()

#   class CFGStudent(<should inherit from Student>)

class CFGStudent(Student):

    def __init__(self, name, age, id, specialization):
        super().__init__(name, age, id)
        self.specialization = specialization

#     create new methods that manage student's subjects (add/remove new subject and its grade to the dict)

    def add_subject(self, subject, grade):
        self.subjects.update({subject: grade})
        print(f"{subject} with grade {grade} has been added to Student ID: {self.id}")

#   Here I tried to add an if/else statement to make sure the subject was in the students record and if not it would
#   give an error print statement, but it then did it for everyone, so I removed it- would love to understand what I did wrong.
    # def remove_subject(self, subject):
    #     if subject == self.subjects:
    #         self.subjects.pop(subject)
    #         print(f"{subject} has been removed from Student ID: {self.id}")
    #     else:
    #         print(f"There is no record of {self.id} taking {subject}.")

    def remove_subject(self, subject):
        self.subjects.pop(subject)
        print(f"{subject} has been removed from Student ID: {self.id}")

#     create a method  (and a new variable) to get student's overall mark (use average)

    def average_grade(self):
        total_grade = sum(self.subjects.values())
        average = total_grade / len(self.subjects)
        print(f"{self.id} has an average grade of {average:.2f}")
        return average

#     create a method to view all subjects taken by a student

    def display_subjects_taken(self):
        print(f"{self.name} is taking {self.subjects}")


if __name__ == '__main__':

    nancy = CFGStudent('Nancy', 18, 95137, 'Software')
    john = CFGStudent('John', 19, 85246, 'Full Stack')
    sam = CFGStudent('Sam', 22, 13795, 'Software')
    nancy.add_subject('Python', 92)
    nancy.add_subject('SQL', 90)
    nancy.add_subject('OOP', 89)
    john.add_subject('Python', 90)
    john.add_subject('OOP', 89)
    sam.add_subject('Python', 94)
    sam.add_subject('SQL', 88)
    nancy.display_subjects_taken()
    sam.display_subjects_taken()
    john.display_subjects_taken()
    nancy.average_grade()
    nancy.remove_subject('OOP')
    nancy.display_subjects_taken()
    nancy.average_grade()
    sam.average_grade()
    john.average_grade()