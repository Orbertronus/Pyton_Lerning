# Домашня робота №19 "Пошук спільних елементів" з курсу "Python Basic"
# Написати функцію common_elements, яка згенерує два списки елементів .
# Один список з числами кратними 3, інший з кратними числами 5.
# Кількість елементів у цих списках може бути різним.
# За допомогою множин створіть набір з числами, які є в обох множинах (перетин).
# Функція повинна повернути цю множину як результат своєї роботи.

import random


def common_elements():
    set3 = {(i + 1) * 3 for i in range(random.randrange(5, 30, random.randint(1, 3)))}
    set5 = {(i + 1) * 5 for i in range(random.randrange(5, 30, random.randint(1, 5)))}
    set3_5 = set3.intersection(set5)
    return set3_5
