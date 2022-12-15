from module_errors import *
from module_person import *
from module_students import *
from module_group import *

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
