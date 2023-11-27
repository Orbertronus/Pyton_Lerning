"""
        Домашня робота №31 "Очистити текст від html-тегів"

 Завдання написати функцію, яка прочитає заданий файл, очистить текст від html-тегів
 і запише цей текст в інший файл.
 html-тег завжди починається з "<" і закінчується на ">" тобто. потрібно видалити ці символи та все,
 що між ними.
 Функція отримує на вхід два параметри – ім'я файлу, який потрібно очистити,
 та ім'я файлу, куди потрібно записати очищений текст.
 Ім'я файлу, куди потрібно писати, можна задати за замовчуванням.

Приклади файлів у вкладенні – файл який потрібно очистити (draft.html) та приклад файлу,
який може вийти на виході з очищеним текстом.
Файл draft.html необхідно скачати і покласти поряд з файлом, де буде вирішення цієї домашки.

Додаткове завдання для тих, хто захоче ускладнити рішення - спробуйте прибрати рядки,
в яких немає інформації.
"""
import codecs


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()
    str_without_tags = ''
    str_without_blanks = ''
    is_tag = False
    for ch in html:
        if ch == '<':
            is_tag = True
        if is_tag is False:
            str_without_tags += ch
        if ch == '>':
            is_tag = False
    is_line_empty = True
    tmp_line = ''
    for ch in str_without_tags:
        tmp_line += ch
        if ch not in [' ', '\n']:
            is_line_empty = False
        if ch == '\n':
            if not is_line_empty:
                str_without_blanks += tmp_line
            tmp_line = ''
            is_line_empty = True
    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write(str_without_blanks[:-1])


delete_html_tags("draft.html")
