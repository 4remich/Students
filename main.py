class GroupLimitError(Exception):
    def __init__(self, max_limit):
        self.max_limit = max_limit

    def __str__(self):
        return f'This group is already exist from {self.max_limit} students.'

class DublicateStudentError(Exception):
    def __init__(self, student, group_title):
        self.student = student
        self.group_title = group_title

    def __str__(self):
        return f'The {self.student} registered in group {self.group_title}.'

class Person:

    def __init__(self, surname: str, name: str, age: int, sex: str, height: float, weight: float,
                 id: int, drive_license: str, email: str, phone: str):
        self.surname = surname
        self.name = name
        self.age = age
        self.sex = sex
        self.height = height
        self.weight = weight
        self.id = id
        self.drive_license = drive_license
        self.email = email
        self.phone = phone

    def __str__(self):
        return f'{self.surname} {self.name}\n{self.age} y.o., {self.sex}\nHeight: {self.height} cm\n' \
               f'Weight: {self.weight} kg\nID: {self.id}\nDrive license#: {self.drive_license}\n' \
               f'E-mail: {self.email}\nPhone: {self.phone}'


class Students(Person):

    def __init__(self, surname, name, age, sex, height, weight, id, drive_license, email, phone, english_level):
        super().__init__(surname, name, age, sex, height, weight, id, drive_license, email, phone)
        self.english_level = english_level

    def __str__(self):
        return f'{self.surname} {self.name}, {self.age} y.o., {self.email}, {self.phone}, {self.english_level}'


class Group:
    def __init__(self, title, max_students=10):
        self.title = title
        self.students = []
        self.max_student = max_students

    def add_student(self, student):

        if len(self.students) >= self.max_student:
            raise GroupLimitError(self.max_student)

        self.students.append(student)


    def remove_student(self, student):
        if student in  self.students:
            self.students.remove(student)

    def search_surname(self, surname):
        list = []
        for student in self.students:
            if student.surname == surname:
                list.append(student)
        return list

    def __str__(self):
        return f'{self.title}\n\n' + '\n'.join(map(str, self.students))

try:

    group_python = Group("Group Python")

    group_python.add_student(Students('Ivanov', 'Ivan', 21, 'male', 173.2, 69.3, 23652514, 'none', 'ii@gmail.com',
                                      '+380447777777', 'B1'))
    group_python.add_student(Students('Ivanov', 'Ivan', 22, 'male', 173.2, 69.3, 23652514, 'none', 'ii@gmail.com',
                                      '+380447777777', 'B1'))
    group_python.add_student(Students('Ivanov', 'Ivan', 23, 'male', 173.2, 69.3, 23652514, 'none', 'ii@gmail.com',
                                      '+380447777777', 'B1'))
    group_python.add_student(Students('Ivanov', 'Ivan', 24, 'male', 173.2, 69.3, 23652514, 'none', 'ii@gmail.com',
                                      '+380447777777', 'B1'))
    group_python.add_student(Students('Ivanov', 'Ivan', 25, 'male', 173.2, 69.3, 23652514, 'none', 'ii@gmail.com',
                                      '+380447777777', 'B1'))
    group_python.add_student(Students('Ivanov', 'Ivan', 26, 'male', 173.2, 69.3, 23652514, 'none', 'ii@gmail.com',
                                      '+380447777777', 'B1'))
    group_python.add_student(Students('Ivanov', 'Ivan', 27, 'male', 173.2, 69.3, 23652514, 'none', 'ii@gmail.com',
                                      '+380447777777', 'B1'))
    group_python.add_student(Students('Ivanov', 'Ivan', 28, 'male', 173.2, 69.3, 23652514, 'none', 'ii@gmail.com',
                                      '+380447777777', 'B1'))
    group_python.add_student(Students('Ivanov', 'Ivan', 29, 'male', 173.2, 69.3, 23652514, 'none', 'ii@gmail.com',
                                      '+380447777777', 'B1'))
    group_python.add_student(Students('Ivanov', 'Ivan', 30, 'male', 173.2, 69.3, 23652514, 'none', 'ii@gmail.com',
                                      '+380447777777', 'B1'))
    group_python.add_student(Students('Ivanov', 'Ivan', 31, 'male', 173.2, 69.3, 23652514, 'none', 'ii@gmail.com',
                                      '+380447777777', 'B1'))
    group_python.add_student(Students('Ivanov', 'Ivan', 32, 'male', 173.2, 69.3, 23652514, 'none', 'ii@gmail.com',
                                      '+380447777777', 'B1'))

except Exception as error:
    print(error)
else:
    print(group_python)

import logging

logger = logging.getLogger('Students.py')
logger.setLevel(logging.ERROR)
fh = logging.FileHandler('logger.log')
fh.setLevel(logging.ERROR)
formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

logger.error('attempt to add an extra student to the group-python')
