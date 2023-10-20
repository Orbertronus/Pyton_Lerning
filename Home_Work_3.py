# Домащня робота № 3, із курсу Python Basic
# На запит від програми, користувач вводить 5-ти значне ціле, позитивне число.
# Необхідно "перевернути" цє число  задом наперед, щоб у результаті вийшло теж 5-ти значне число,
# але із зворотною послідовністю цифр.
# Приклади:  Користувач ввів: 12345 - на екрані відображається: 54321
num = int(input("Введіть п'ятизначне число :"))
x, y = divmod(num, 10_000)  # починаемо "розбирати" число на складові
N_5 = x                     # результат  цілочисленного ділення (кількість десятитисячних часток) запам'ятовуемо
                            # це будена наша крайня права літера в результаті на 5му  місці
x, y = divmod(y, 1000)      # беремо остачу від минулої операції - чотирьохзначне число у і
                            # продовжуємо діставати крайню ліву літеру числа
N_4 = x                     # результат (кількість тисячних часток від минулої остачі)
                            # буде стояти на передостанньму 4 му місці числа результата
x, y = divmod(y, 100)       # беремо остачу (трьохзначне число) і повторюемо але уже зі сотками
N_3 = x                     # результат буде на третьому місці - замам'ятовуємо
N_2, N_1 = divmod(y, 10)    # остачу (двохзначне число) одразуж однією операціею
                            # розподіляємо між результуючими змінними
print((N_1 * 10_000)+(N_2 * 1000)+(N_3 * 100)+(N_4 * 10) + N_5) # кожна змінна має своє "вагове" місце в розряді
# тому  здійснюючі єлементарні операції і враховуючи ваговий коефіцієнт розряду  -
# збираємо із основних складових наше число - результат, безпосередньо у функціі виводу на єкран

