while True:
    word = input("напишите слово на кирилице или на латинице (пример:'слово')     если хотите выйти то напишите 'стоп' ")
    if word.lower() == "стоп":
        break
    common_sum_letters = len(word)
    glasnye = 0
    soglasnye = 0
    for letter in word:
        if letter.lower() in "aeiouаеёиоуыэюя":
            glasnye += 1
        elif letter.isalpha():
            soglasnye += 1
    percentage_glasnye = round((glasnye / common_sum_letters) * 100, 2)
    percentage_soglasnye = round((soglasnye / common_sum_letters) * 100, 2)
    print("common_sum_letters:", common_sum_letters)
    print("glasnye:", glasnye)
    print("soglasnye:", soglasnye)
    print("Percentage of glasnye:", percentage_glasnye, "%")
    print("Percentage of soglasnye:", percentage_soglasnye, "%")

#     списки
#     завернуты
#     в
#     квадратных
#     скобках
#     методы: append -
# numbers = [21, 34, 54, 12]
#
# print("Before Append:", numbers)
#
# # Использование метода append()
# numbers.append(32)
#
# print("After Append:", numbers)
# Список может содержать любое количество элементов,
# и они могут быть разных типов (int, float, string и т.д

# languages = ["Python", "Swift", "C++"]
#
# # Получаем доступ к элементу под индексом 0
# print(languages[0])  # выведет Python
#
# # Получаем доступ к элементу под индексом 2
# print(languages[2])  # выведет C++

# Срез списка в Python

# my_list = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z']
#
# # Выводим "срезанные" элементы со 2 по 4 индекс
# print(my_list[2:4])
#
# # Выводим "срезанные" элементы от индекса 5 и до конца списка
# print(my_list[5:])
#
# # Выводим все элементы списка
# print(my_list[:])
# prime_numbers = [2, 3, 5]
# print("List1:", prime_numbers)
#
# even_numbers = [4, 6, 8]
# print("List2:", even_numbers)
#
# # Объединение двух списков
# prime_numbers.extend(even_numbers)
#
# print("List after append:", prime_numbers)
def print_list_item(index, lst=None):
    if lst is None:
        lst = list(range(1, 11))
    while True:
        try:
            print(lst[index])
            break
        except IndexError:
            print("Указан неверный индекс!")
            print("Введите один из следующих индексов:", end=" ")
            for i in range(len(lst)):
                print(i, end=" ")
            print()
            index = int(input("Введите новый индекс: "))