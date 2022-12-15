from module_person import *

class Students(Person):

    def __init__(self, surname, name, age, sex, height, weight, id, drive_license, email, phone, english_level):
        super().__init__(surname, name, age, sex, height, weight, id, drive_license, email, phone)
        self.english_level = english_level

    def __str__(self):
        return f'{self.surname} {self.name}, {self.age} y.o., {self.email}, {self.phone}, {self.english_level}'

