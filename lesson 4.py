# p = 0
# while True:
#     p += 1
#     im1 = int(input('Вееди число: '))
#
#     if type(im1) == int:
#         if im1 > 10:
#             print('оно больше 10')
#         if im1 == 10:
#             print('оно равна 10')
#         else:
#             print('меньше 10')
#     else:
#         print('это не число')

while True:
    word = input("Введите слово на латинице или кириллице (для выхода введите 'exit'): ")

    if word.lower() == 'exit':
        print("Программа завершена.")
        break

    total_letters = len(word)
    consonants = 0
    vowels = 0

    for letter in word:
        if letter.isalpha():
            if letter.lower() in ['a', 'e', 'i', 'o', 'u', 'y', 'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']:
                vowels += 1
            else:
                consonants += 1

    vowel_percentage = (vowels / total_letters) * 100
    consonant_percentage = (consonants / total_letters) * 100

    print("Общее количество букв:", total_letters)
    print("Количество согласных букв:", consonants)
    print("Количество гласных букв:", vowels)
    print("Процентное соотношение гласных букв: {:.2f}%".format(vowel_percentage))
    print("Процентное соотношение согласных букв: {:.2f}%".format(consonant_percentage))

while True:
    word = input('enter any word: ').lower()
    vowels = 0
    consonants = 0
    print('letter count:', len(word))

    for i in word:
        if i == 'a' or i == 'e' or i == 'o' or i == 'i' or i == 'u':
            vowels = vowels + 1
        else:
            consonants = consonants + 1
    print('number of vowels: ', vowels)
    print('number of consonants: ', consonants)

    v = str(round(vowels / (vowels + consonants) * 100, 2))
    c = str(round((consonants / (vowels + consonants)) * 100, 2))

    print('vowel/consonant ratio', v, '/', c)







