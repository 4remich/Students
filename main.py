
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
        return f'{self.surname} {self.name}, {self.age} y.o.\n{self.email}\n{self.phone}' \
               f'\nEnglish level: {self.english_level}'


class Group:
    def __init__(self, title, max_students=10):
        self.title = title
        self.students = []
        self.max_student = max_students

    def add_student(self, student):
        if student not in self.students and len(self.students) < self.max_student:
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
        return f'{self.title}\n' + '\n'.join(map(str, self.students))


group_python = Group("Group Python")

group_python.add_student(Students('Ivanov', 'Ivan', 19, 'male', 173.2, 69.3, 23652514, 'none', 'ii@gmail.com',
                                  '+380447777777', 'B1'))




