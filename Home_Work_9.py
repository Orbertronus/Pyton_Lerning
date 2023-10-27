# Домашня робота №9 із курсу "Python Basic"
# Створіть список випадкових чисел із випадковою кількістю елементів від 3 до 10.
# Ваше завдання - створити новий список з 3 елементів початкового списку -
# першим, третім і другим з кінця.
#Приклад:
#[1, 2, 3, 4, 5, 6, 7, 9] == [1, 3, 7]
#[1, 1, 2, 1] == [1, 2, 2]
#[6, 3, 7] == [6, 7, 3]
import random
lst = []
for i in range(random.randint(3,10)):
    lst.append(random.randint(0,10))
print(lst, end=' == ')
lst_rezult=[]
lst_rezult.append(lst[0])  # додаємо перший елемент
lst_rezult.append(lst[2])  # третій
lst_rezult.append(lst[-2])  # і другий з кінця
print(lst_rezult)