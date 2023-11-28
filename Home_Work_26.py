"""
    Домашня робота №26 "Знайти перше слово"

    Написати функцію first_word, яка у  переданому рядку знайде її перше слово.
 При розв'язанні задачі звернути увагу на наступні моменти:
    - У рядку можуть зустрічаються крапки та / або коми
    - Рядок може починатися з літери або, наприклад, зпробілу або точки
    - У слові може бути апостроф і він є частиною слова
    - Весь текст може бути представлений лише одним словом та все

Вхідні
параметри: Рядок.
Вихідні
параметри: Рядок.
"""


def first_word(text):
    """ Пошук першого слова """
    return text.replace('.', ' ').replace(',', '').split()[0]


assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')
