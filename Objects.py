class Student:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return "is on honor roll"
        else:
            return "is on honor roll"


class SpecialStudent(Student):
    def __init__(self, name, major, gpa, is_on_probation, speciality):
        Student.__init__(self, name, major, gpa, is_on_probation)
        self.speciality = speciality


student1 = Student("jim", "business", 3.1, False)
student2 = SpecialStudent("steve", "managment", 3.8, True, "creativity")
print(student1.name)
print(student1.major)
print(student1.gpa)
print(student1.is_on_probation)
print(student1.name + " " + student1.on_honor_roll())
print(student2.name)
print(student2.major)
print(student2.gpa)
print(student2.is_on_probation)
print(student2.speciality)

print(student2.name + " " + student2.on_honor_roll())
