# Домашня робота №12 з курсу "Python Basic"
#  Користувач вводить рядок. Завдання – перетворити рядок на hashtag.
# Декілька правил:
# 1) ніяких символів з набору string.punctuation не повинно бути, у тому числі й пробілів;
# 2) підсумкова довжина hashtag має бути не більше 140 символів.
# 3) кожне слово починається з великої літери.
# 4) якщо довжина хештегу більше 140 символів - обрізати підсумковий рядок до 140 символів.
# Приклади:
#  'Python Community' -> #PythonCommunity
#  'i like python community!' -> #ILikePythonCommunity
#  'Should, I. subscribe? Yes!' -> #ShouldISubscribeYes
import string
strg = input().replace(' ', '')
hsh = "#"
for ch in strg:
    if ch not in string.punctuation:
        hsh += ch
if len(str) > 140:
    hsh = hsh[0:139]
print(hsh)
