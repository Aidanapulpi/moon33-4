data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')

letters = []
numbers = []

for item in data_tuple:
    if type(item) == str:
        letters.append(item)
    else:
        numbers.append(item)

numbers.remove(6.13)
letters.append(letters.pop(0))
numbers.insert(1,2)
numbers.sort()
letters.reverse()
letters[1] = 'G'
letters[-2] ='c'
for i in range(len(numbers)):
     numbers[i]*=numbers[i]
numbers = tuple(numbers)
letters = tuple(letters)
print(letters)
print(numbers)


