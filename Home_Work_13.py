# Домашня робота № 13 "Діапазон букв" з курсу "Python Basic"
# Користувач вводить через дефіс дві літери.
#   Завдання: написати програму, яка повертатиме всі символи між ними включно.
# Жодних перевірок на помилку робити не треба,
# мінімальне значення завжди менше або дорівнює максимальному.
#   Підказка: Використовуйте модуль string , у якому є string.ascii_letters, з усім набором потрібних букв
#   Приклади:
#           "a-c" -> abc
#           "a-a" -> a
#           "s-H" -> stuvwxyzABCDEFGH
#           "a-A" -> abcdefghijklmnopqrstuvwxyzA
import string
in_str = input('Введіть через дефіз дві літери:')
in_lst = in_str.replace('-', ' ').split()    # замінюємо дефіз '-' на ' '
# і за допомогою ф. split() розподіляемо 2 значення в одному рядку між 2 ма елементами списку
r_start = string.ascii_letters.find(in_lst[0])      # в  наведенному наборі букв отримуємо індескс входження
# символу - початку діапазону
r_end = string.ascii_letters.find(in_lst[1]) + 1     # отримуємо індекс кінця діапазону із
# урахуванням особливості зрізу яким ми скористаємося для виведення всих значень діапазону букв
print(string.ascii_letters[r_start:r_end])
