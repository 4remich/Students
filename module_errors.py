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
