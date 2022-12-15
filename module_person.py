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