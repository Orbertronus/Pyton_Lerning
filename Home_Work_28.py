"""
    Домашня робота №28 Генератор простих чисел

    Напишіть функцію-генератор prime_generator, яка повертатиме прості числа.
    Верхня межа цього діапазону визначається параметром цієї функції.

 """
from inspect import isgenerator


def is_prime(num, primes):
    # числа що більше 10 і закінчуються на 2 або 5 не є простими
    if (num > 10) and (num % 10 == 5):
        return False
    for i in primes:
        # числа що діляться націло на інше просте число, окрім себе теж не є простими
        if num % i == 0:
            return False
    return True


def prime_generator(end):
    primes = []
    for i in range(2, end + 1):
        if is_prime(i, primes):
            # для оптимізації роботи алгоритму будемо заносити прості числа в список
            # на основі якого  скористаємось в ф. is_prime(num, primes) перевіряючи наступні числа,
            # ажде за теорією шукати дільники потрібно саме серед ряду попередніх простих чисел
            primes.append(i)
            yield i


gen = prime_generator(1)
assert isgenerator(gen) is True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')
