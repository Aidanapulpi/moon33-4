
var1 = 0
var2 = 0

while True:
    num = int(input('Введите число: '))

    if num == 42:
        print('Программа завершена.')
        break


    elif num % 2 == 0:
        print('Чётное число')
        var1 += num
        if num % 5 == 0:
            print('Кратное 5')
    elif num % 2 != 0:
        print('Нечётное')
        var2 += num

    elif var1 > 50 or var2 > 50:
        print('Программа завершена.')
        break
