# width = 5
# lenth = 8
# square_2 = width * lenth
# print(square_2)
#
# width = 12
# lenth = 18
# square_hall = width * lenth
# print(square_hall)
#  def greet
# print(print.__doc__)

# print(print.__doc__)
# print(len.__doc__)
numbers = [5, 4, 5]
def summa(numbers):
    amount = 0
    for num in numbers:
        amount += num
    return amount

print(summa(numbers))

def custom_min(items):
    min_value = items[0]
    for item in items[1::]:
        if item < min_value:
            min_value = item
    return min_value


numbers = [5, 2, -8, 1, 9]
result = custom_min(numbers)
print("Минимальное значение:", result)


def max1 (items):
    maximum = 0
    lst = []
    for item in items:
        if item > maximum:
            maximum = items
    return maximum

print(max(2, 6, 73, 8, 13))




# когда мы умножаем начальное значение должно быть равно 1, то
# если сделаем равное 0 то число будет возвращаться 0
*= это позволяет нам поочередно умножать и накапливать  результат в  переменнойamount
функция аргс может принимать неограниченное количество аргументов

