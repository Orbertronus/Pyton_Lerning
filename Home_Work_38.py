"""
    Домашня робота № 38
    Створіть клас «Правильний дріб» та реалізуйте методи для екземплярів цього класу:

       - порівняння,
       - додавання,
       - віднімання
       - множення

"""


class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def leas_com_mult(self, do):

        '''
        функція пошуку найменьшого спільного дільника між  першим та другим параметрами
        :param do: перше число і друге (цілі)
        :return: НСД
        '''

        ds = self.b
        lcm = 2
        while lcm <= max(do, ds):
            if ds % lcm == 0 and do % lcm == 0:
                return lcm
            lcm += 1
        return None

    def reduce(self):
        '''
        Функція скорочення дробу
        перезаписує вбудовані змінні a та b
        :return: єкземпляр Fraction
        '''
        a = self.a
        b = self.b

        if b % a == 0:
            a, b = 1, int(b / a)
        else:
            lcm = (self.leas_com_mult(b))
            if lcm != b and lcm < a:
                a = int(a / lcm)
                b = int(b / lcm)
        self.a, self.b = a, b
        return self

    def __mul__(self, other):
        sa = self.a
        sb = self.b
        oa = other.a
        ob = other.b
        return Fraction(sa * oa, sb * ob)

    def common_denominator(self, other):
        """
        Функція пошуку найбільшого спільного дільника
        :param other: int, int
        :return: int
        """
        ds = self.b
        do = other.b

        if ds == do:
            return ds
        while ds >= do:
            if ds % do == 0:
                return ds
            ds += self.b
        while do >= ds:
            if do % ds == 0:
                return do
            do += other.b

        return None

    def __add__(self, other):
        sa = self.a
        sb = self.b
        oa = other.a
        ob = other.b
        cd = ob * sb
        return Fraction(int(sa * (cd / sb) + oa * (cd / ob)), cd)

    def __sub__(self, other):
        sa = self.a
        sb = self.b
        oa = other.a
        ob = other.b
        cd = ob * sb
        return Fraction(int(sa * (cd / sb) - oa * (cd / ob)), cd)

    def __eq__(self, other):
        if isinstance(other, Fraction):
            self.reduce()
            other.reduce()
            return self.a == other.a and self.b == other.b
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Fraction):
            return self.a / self.b > other.a / other.b
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Fraction):
            return self.a / self.b < other.a / other.b
        return NotImplemented

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"


f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == 'Fraction: 21, 18'
f_d = f_b * f_a
assert str(f_d) == 'Fraction: 6, 18'
f_e = f_a - f_b
assert str(f_e) == 'Fraction: 3, 18'

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True
print('OK')
