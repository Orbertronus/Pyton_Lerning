# Ваша програма має перенести останній елемент списку з кінця на початок,
# тобто, останній елемент списку має стати першим.
# Послідовність інших елементів не має змінюватися.
# Порожній список або список з одним елементом повинен залишитися незмінним.
# Кількість елементів у списку може бути будь-яким – нуль та більше!
# Приклади
# [12, 3, 4, 10] => [10, 12, 3, 4]
# [1] => [1]
# [] => []
# [12, 3, 4, 10, 8] => [8, 12, 3, 4, 10]
# Робити запит на введення даних від користувача не потрібно.
lst = list(input())
if len(lst):
    lst.insert(0,lst.pop()) # _index: - транслятор сам підставив
print(lst)