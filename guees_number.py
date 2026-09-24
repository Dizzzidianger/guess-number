# угадай число (пк загадывает число а пользователь должен угадать какое именно)

import random

# рандомайзер 
numbers = random.randint(1, 12)

tryes  = 0 # счетчик попыток

# Логика с угадыванием больше или меньше

while True:
    print("пк загодал число от 1 до 12, нужно угадать число")

    # Проверка на ввод
    try:
        answer = int(input())         
    except ValueError:
        print("Введите число!")
        break

    if answer == numbers:
        print(f"Вы угадали число с: {tryes} попытки! ")
        break
    else:
        if numbers > answer:
            print("Вы не угадали, пк загадал число больше вашего")
            tryes += 1
            continue
            
        if numbers < answer:
            print("Вы не угадали, пк загадал число меньше вашего")
            tryes += 1
            continue
            




