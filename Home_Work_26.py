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

import string


def cut_s_ptn(txt):
    i = 0
    for ch in txt:
        if ch in string.punctuation and ch not in "'":
            return txt[:i], i
        i += 1
    return txt, i
def first_word(text):
    """ Пошук першого слова """
    ind = 0
    i = 0

    while True:
        ind = text.find(' ',ind)

        if ind == -1:
        # випадок коли не знайдено пробілу. обріжемо по знак пунктуації
            res_txt, ind = cut_s_ptn(text)
        else:
            # коли пробіл є, здійснюємо здріз
            res_txt, i = cut_s_ptn(text[i: ind])

        if len(res_txt) > 0 or ind == len(text):
            return res_txt

        ind += 1
        i = ind


assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')
