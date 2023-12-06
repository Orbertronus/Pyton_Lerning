"""
        Домашня робота №37 "Клас прямокутник"

    Створити клас «Прямокутник», у якого  необхідно реалізувати два поля(ширина та висота)
    та кілька обов'язкових методів:
        Метод  порівняння прямокутників за площею.
        Метод  складання прямокутників
                (площа  сумарного прямокутника повинна  дорівнювати сумі площ прямокутників, які ми складаємо).
        Методи множення прямокутника на число n (це має збільшити площу базового прямокутника в n разів).
    У класі можуть бути створені додаткові(допоміжні методи)

    Декілька уточнень:

            1. Методи складання, множення, поділу тощо.обов'язково маємо повертати новий екземпляр класу Прямокутник!
            2. Для множення, додавання, порівняння, обов'язково потрібно перевизначати "магічні" методи.
                Для множення є вбудований метод __mul__
            3. Коли в результаті мат.дій створюєте новий екземпляр класу Прямокутник, то у цього екземпляру,
                перемноження сторін, має давати необхідну площу.Це теж важливо

"""


class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        if isinstance(other, (int, float)):
            return self.width == other and self.height == other
        if isinstance(other, (list, tuple)):
            return self.width == other[0] and self.height == other[1]
        if isinstance(other, set):
            # дістанемо елементи множини методом pop() видалення із поверненням
            sw, sh = other.pop(), other.pop()
            # повернемо значення множини назад відновивши її початковий стан
            other.__init__({sw, sh})
            # порівняємо збереженні значення із данними прямокутника
            return self.width == sw and self.height == sh
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Rectangle):
            # Скоротимо (спростимо) назви змінних
            sw = self.width
            sh = self.height
            ow = other.width
            oh = other.height
            #  додаємо сторони пряокутників за принципом: наклавши одноіменні сторони одна на одну
            #  (т.ч. у нас буде однакова  спільна ширина по меньшій величині із двох ширин прямокутників )
            #  а добуток різниці шинин (від більшої до меньшої) ділимо на висоту спільної меньшої
            #  ширини
            if sw <= ow:
                return Rectangle(sw, int(sh + oh + ((ow - sw) * oh)/sw))

            if sw > ow:
                return Rectangle(ow, int(sh + oh + ((sw - ow) * sh)/ow))
        if isinstance(other, str):
            return f'{str(self)} {other}'
        return NotImplemented

    def __iadd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        if isinstance(other, Rectangle):
            return Rectangle(self.width * other.width, self.height * other.height)
        if isinstance(other, (int, float)):
            return Rectangle(int(self.width * (other/2)), int(self.height * (other/2)))
        return NotImplemented

    def __str__(self):
        return f'{self.__class__.__name__} має ширину: {self.width}, висоту: {self.height}'


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)

assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2

print(r1 + 'r1')
print('Square r3='+str(r3.get_square()))
assert r3.get_square() == 26, 'Test3'
r3_1 = r2 + r1
assert r3_1.get_square() == r2.get_square() + r1.get_square(), 'Test3_1'
r3_2 = r3 + r3_1

assert r3_2.get_square() == r3.get_square() + r3_1.get_square(), 'Test3_2'

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'

r5 = Rectangle(3, 6)
assert r5 == r2, 'Test5'

r6 = Rectangle(3, 3)
assert r6 == 3, 'Test6'
assert r6 == [3, 3], 'Test6.1'
assert r6 == (3, 3), 'Test6.2'

ls_t = [3, 6]
t_t = (2, 4)
s_t = {2, 4}
r7 = Rectangle(7.212, 7.212)
assert r7 == 7.212, 'Test7'
assert r5 == ls_t, 'Test7.1'
assert r1 == t_t, 'Test7.2'
assert r1 == s_t, 'Test7.3'
print(f'Множина {s_t} після порівняння')
print('Ok')
