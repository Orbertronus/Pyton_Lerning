class MaxStudentException(Exception):
    """
    Клас - виняток. Реалізація обробки ситуації
    по перевищенню максимально допустимої кількості студентів у группі
    """

    def __init__(self, message, val):
        super().__init__()
        self.message = message
        self.val = val

    def get_except_msg(self):
        return self.message
