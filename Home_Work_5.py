# Розділити один список на два списки
# Програма повинна вміти розділяти один список на два та помістити їх у новий список.
# Тобто, в результаті повинен вийти список із 2-х списків.
# Якщо в початковому списку непарна кількість елементів, то в першому списку має бути більше елементів.
# Якщо у списку немає елементів, то має бути створений список із двома порожніми списками.
# Потрібно створити рішення, яке обробляє 3 випадки - список порожній,
# у списку парна кількість елементів і в списку непарна кількість елементів.
# Приклади:
# Було => стало
# [1, 2, 3, 4, 5, 6] => [[1, 2, 3], [4, 5, 6]]
# [1, 2, 3] => [[1, 2], [3]]
# [1, 2, 3, 4, 5] => [[1, 2, 3], [4, 5]]
# [1] => [[1], []]
# [] => [[], []]
# Робити запит на введення даних від користувача не потрібно.

lst = list(input())# введення початкового списку данних
lst_rez = [[], []] # ініціалізація результуючго списку я пустого
end = len(lst)
if end:            # перевірка на випадок коли початковий список не порожній
    if len(lst) % 2:            # якщо елементів у початковому списку непарна кількість
        mid = int(len(lst)/2)+1 # обчислюемо індекс центру поділу непарного списку
    else:                       # коли елементів у поч. списку парна кількість
        mid = int(len(lst) / 2) # обчислюемо індекс центру поділу парного списку
    lst_rez[0] = lst[0:mid]     # в перший елемент списку - результата заносимо
                                # першу половину (зріз) початкогово списку
    lst_rez[1] = lst[mid:end]   # в другий елемент списку заносиму другу половину
print(lst_rez)
