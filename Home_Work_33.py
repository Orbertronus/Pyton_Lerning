"""
    Домашня робота №33 "Группа студентів"

    1) Створити клас, що описує людину (створити метод, що виводить інформацію про людину).
    2) На його основі створіть клас Студент (перевизначити метод виведення інформації).
    3) Створити клас Група, екземпляр якого складається з об'єктів класу Студент.
        Реалізувати методи додавання, видалення студента та метод пошуку студента на прізвище.

    * Метод пошуку студента повинен повертати саме екземпляр класу Студент, якщо студент є у групі, інакше - None.
    * У методі видалення, використовувати результат методу пошуку. Тобто. потрібно скомбінувати ці два методи;
    * Визначити для групи метод __str__() для повернення списку студентів у вигляді рядка.

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

    def add_student(self, student):
        self.group.add(student)

    def delete_student(self, last_name):
        self.group.discard(self.find_student(last_name))

    def find_student(self, last_name):
        for instance in self.group:
            if instance.last_name == last_name:
                return instance
        return None

    def __str__(self):
        all_students = ''
        for std in self.group:
            all_students += f'{std.first_name} {std.last_name}, {std.gender} {std.age}\n'
        return f'Number:{self.number}\n {all_students} '


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!
