"""
    Домашня робота №35 "Группа студентів. Виняток користувача"

    Модифікуйте клас Група (завдання минулої лекції) так, щоб при спробі додавання до групи більше 10-ти студентів,
    було порушено виняток користувача.
    Таким чином потрібно створити ще й виняток користувача для цієї ситуації. І обробити його поза межами класу.
    Тобто. потрібно перехопити цей виняток, при спробі додавання 11-го студента


"""


class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.age = age
        self.gender = gender
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name}{self.last_name} {self.gender}, {self.age} років'


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'{super().__str__()}{self.record_book}'


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()
        self.total_students = 0

    def add_student(self, student):
        if self.total_students == 10:
            raise MaxStudentException("Досягнуто максимальної кількості 10 студентів в групі!", self.total_students)
        self.total_students += 1
        self.group.add(student)

    def delete_student(self, last_name):
        if self.find_student(last_name) is not None:
            self.group.discard(self.find_student(last_name))
            self.total_students -= 1
            return 0
        return -1

    def find_student(self, last_name):
        for instance in self.group:
            if instance.last_name == last_name:
                return instance
        return None

    def __str__(self):
        all_students = ''
        for std in self.group:
            all_students += f'{std.first_name} {std.last_name}, {std.gender} {std.age}\n'
        all_students += f'Total students: {self.total_students}\n'
        return f'Number:{self.number}\n {all_students} '


class MaxStudentException(Exception):

    def __init__(self, message, val):
        super().__init__()
        self.message = message
        self.val = val

    def get_except_msg(self):
        return self.message


st = [
       Student('Male', 30, 'Steve', 'Jobs', 'AN142'),
       Student('Female', 25, 'Liza', 'Taylor', 'AN145'),
       Student('Male', 30, 'Klark', 'Denits', 'AL102'),
       Student('Female', 26, 'Klara', 'Chasten', 'AK012'),
       Student('Male', 31, 'Roy', 'Shneider', 'AS120'),
       Student('Male', 29, 'Bruse', 'Roberts', 'DN781'),
       Student('Male', 28, 'Lorn', 'Olbernt', 'LD802'),
       Student('Female', 27, 'Sarah', 'Parker', 'AP002'),
       Student('Female', 27, 'Andrea', 'Wells', 'AW095'),
       Student('Male', 34, 'Robert', 'Dapt', 'RN027'),
       Student('Male', 23, 'Stan', 'Ipkins', 'SN005'),
       Student('Male', 23, 'Ethan', 'Price', 'IN855')
       ]
gr = Group('PD1')
try:
    for ind in range(len(st)):
        gr.add_student(st[ind])
except MaxStudentException as err:
    print(err.message)
print(gr)

# стосовно коду нижче ніяких вказівок не було, тому функціонал лишаю
assert str(gr.find_student('Jobs')) == str(st[0]), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)

gr.delete_student('Taylor')  # No error!
