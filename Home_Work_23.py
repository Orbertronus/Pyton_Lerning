"""
    Домашня робота №23 "Популярність слів у тексті"

   На вхід функції popular_words передаються два аргументи: текст та список слів,
   популярність яких необхідно визначити.
   Умови:
    - Слова необхідно шукати у всіх регістрах.
    - Якщо слово не знайдено жодного разу, його необхідно повернути у словнику зі значенням 0 (нуль)

   Вхідні параметри: Текст і масив слів, що шукаються.

   Вихідні параметри: Словник, у якому ключами є шукані слова та значеннями, скільки разів кожнє слово
   зустрічаються у орігінальному тексті.

"""


def popular_words(text, words):
    text = text.lower().split()
    return {w: text.count(w) for w in words}


assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
print('OK')
