# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

import random
while True:
    try:
        n = int(input('Введите число монеток: '))
        heads, tails = 0,0
        for i in range(n):
            coin = random.randint(0,1)
            if coin == 0:
                heads += 1
            else:
                tails += 1
        print(f'Нужно перевернуть {min(heads, tails)} монет.')
    except Exception:
        print('Неверный ввод!')
