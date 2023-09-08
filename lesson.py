number = 34
running = True
while running:
    guess = int(input('Введите целое число'))
    if guess == number:
        print('Поздравляю, вы угадали!')
        running = False
    elif guess < number:
        print('Нет, загаданное число больше этого')
    else:
        print('Нет, загаданное число немного меньше этого.')
else:
    print('Цикл while закончен.')
print('Завершение.')



