# Домащня робота № 21 "Паліндром" з курсу "Python Basic"
# Завдання – написати функцію is_palindrome, яка перевірятиме,
# чи є рядок паліндромом. Паліндромом - це такий рядок, який читається
# однаково зліва направо і зправа наліво без урахування знаків пунктуації
# та розмірності букв.
#  Функція приймає на вхід рядок, та повертає булеве значення True або False
import string


def is_palindrome(text):
    # підготуємо рядок до перевірки видаливши всі символи пунктуації, пробіли
    # та перевівши всі букви в один регістр
    text = text.replace(' ', '').lower()
    for x in string.punctuation:
        text = text.replace(x, '')
    # за допомогою зрізів перевіряємо обидві частини і повертаємо результат
    return text[0:len(text)//2] == text[-1:len(text)//2:-1]


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
