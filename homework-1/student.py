"""

TASK 2

Write a base class to represent a student. Below is a starter code.
Feel free to add any more new features to your class.
As a minimum a student has a name and age and a unique ID.

Create a new subclass from student to represent a concrete student doing a specialization, for example:
Software Student and Data Science student.


"""

class CFGStudent:

    def __init__(self):
        self.name = {}
        self.age = 0
        self.id = {}
        self.subjects = dict()
        self.grade = None

    def add_student(self, name, age, id, subject, grade=None):
        self.name = name
        self.age = age
        self.id = id
        self.subjects = subject
        self.grade = grade

    def add_subject(self,subject, grade):
        self.subjects.update({subject: grade})
        print(f"{subject} with grade {grade} has been added to Student ID: {student_id}")

    def remove_subject(self, student_id, subject):
        if student_id == student_id:
            self.subjects.pop(subject)
            print(f"{subject} has been added to Student ID: {student_id}")

    def average_grade(self, grade, subjects):
        total_grade = sum(grade)
        total_grade / len(subjects)

    def display_subjects_taken(self):
            print('Name', self.name)
            print('age', self.age)
            print('id', self.id)
            print('subjects', self.subjects)
            print('subjects', self.grade)

if __name__ == '__main__':
    student_list = CFGStudent()
    student_list.add_student('Nancy', 18, 95137, 'Software', 99)
    student_list.add_student('John', 19, 85246, 'Full Stack', 92)
    student_list.add_student('Sam', 22, 13795, 'Software', 98)
    print(student_list.display_subjects_taken())
    student_list.add_subject('Full Stack', 92)
    student_list.display_subjects_taken()


# class CFGStudent(<should inherit from Student>)
#     create new methods that manage student's subjects (add/remove new subject and its grade to the dict)
#     create a method to view all subjects taken by a student
#     create a method  (and a new variable) to get student's overall mark (use average)