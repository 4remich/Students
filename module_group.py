from module_errors import *

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
