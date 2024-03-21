class Student:
    def __init__(self, name, age, grade, courses):
        self.name = name
        self.age = age
        self.grade = grade
        self.courses = courses
        if not isinstance(courses, list):
            raise TypeError("Name must be a list")

    def add_course(self, new_course):
        self.courses.append(new_course)


a = Student('alex', 19, 4, ['a', 'b', 'c'])
a.add_course('f')
print(a.courses)
