"""

In the selected code, you see the definition of a Student class. When a Student object is created,
it is initialized with a name, year, and an empty list of grades. The add_grade method allows you to add a Grade
object to the grades list if it has the correct Grade type.

"""


class Student:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.grades = []

    def add_grade(self, grade):
        if type(grade) is Grade:
            self.grades.append(grade)


class Grade:
    minimum_passing = 65

    def __init__(self, score):
        self.score = score


roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)
pieter.add_grade(Grade(100))
