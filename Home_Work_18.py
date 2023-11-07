# Домашня робота №18 "Пошук підрядка" з курсу "Python Basic"
#  Функція second_index приймає як параметри 2 рядки. Необхідно знайти індекс
#  другого входження шуканого рядка у рядку для пошуку.
#
# Input: Два рядки (String).
# Output: Int or None

def second_index(text, some_str):
    i = text.find(some_str)  # індекс першого входження
    i = text.find(some_str, i + 1)  # індекс другого входження починаючи після першого
    return None if (i == -1) else i


assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')
