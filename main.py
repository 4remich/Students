
class Person:

    def __init__(self, surname: str, name: str, age: int, sex: str, height: float, weight: float,
                 id: int, drive_license: str, english_level: str, email: str, phone: str):
        self.surname = surname
        self.name = name
        self.age = age
        self.sex = sex
        self.height = height
        self.weight = weight
        self.id = id
        self.drive_license = drive_license
        self.english_level = english_level
        self.email = email
        self.phone = phone

    def __str__(self):
        return f'{self.surname} {self.name}\n{self.age} y.o., {self.sex}\nHeight: {self.height} cm\n' \
               f'Weight: {self.weight} kg\nID: {self.id}\nDrive license#: {self.drive_license}\n' \
               f'English level: {self.english_level}\nE-mail: {self.email}\nPhone: {self.phone}'


class Students(Person):

    def __init__(self):
        super().__init__()

    def __str__(self):
        return f'{self.surname} {self.name}\nEnglish level: {self.english_level}\n{self.email}\n{self.phone}'


class Group(Students):

    def __init__():
        super().__init__()
        self.title = title
        self.students = []

    def add_student(self, student: Students):
        if student in self.students:
            index = self.students.index(student)
        else:
            self.students.append(student)


group_python = Group()

group_python
group_python
group_python
group_python
group_python

person_1 = Person('Ivanov', 'Ivan', 18, 'male', 173.2, 69.3, 23652514, 'none', 'B1', 'ii@gmail.com', '+380447777777')
person_2 = Person('Ivanov', 'Ivan', 19, 'male', 173.2, 69.3, 23652514, 'none', 'B1', 'ii@gmail.com', '+380447777777')
person_3 = Person('Ivanov', 'Ivan', 20, 'male', 173.2, 69.3, 23652514, 'none', 'B1', 'ii@gmail.com', '+380447777777')
person_4 = Person('Ivanov', 'Ivan', 21, 'male', 173.2, 69.3, 23652514, 'none', 'B1', 'ii@gmail.com', '+380447777777')
person_5 = Person('Ivanov', 'Ivan', 22, 'male', 173.2, 69.3, 23652514, 'none', 'B1', 'ii@gmail.com', '+380447777777')
person_6 = Person('Ivanov', 'Ivan', 23, 'male', 173.2, 69.3, 23652514, 'none', 'B1', 'ii@gmail.com', '+380447777777')
person_7 = Person('Ivanov', 'Ivan', 24, 'male', 173.2, 69.3, 23652514, 'none', 'B1', 'ii@gmail.com', '+380447777777')
person_8 = Person('Ivanov', 'Ivan', 25, 'male', 173.2, 69.3, 23652514, 'none', 'B1', 'ii@gmail.com', '+380447777777')
person_9 = Person('Ivanov', 'Ivan', 26, 'male', 173.2, 69.3, 23652514, 'none', 'B1', 'ii@gmail.com', '+380447777777')
person_10 = Person('Ivanov', 'Ivan', 27, 'male', 173.2, 69.3, 23652514, 'none', 'B1', 'ii@gmail.com', '+380447777777')
person_11 = Person('Ivanov', 'Ivan', 28, 'male', 173.2, 69.3, 23652514, 'none', 'B1', 'ii@gmail.com', '+380447777777')
person_12 = Person('Ivanov', 'Ivan', 29, 'male', 173.2, 69.3, 23652514, 'none', 'B1', 'ii@gmail.com', '+380447777777')


# print(person_10)

