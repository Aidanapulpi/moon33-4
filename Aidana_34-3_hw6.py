def mult(*args):
    amount = 1
    for num in args:
        amount *= num
    return amount
print(mult(2, 3, 77,12))


def mirror_string(string, word="hello"):
    if word != "hello":
        return False
    else:
        return string == string[::-1]

stroka = mirror_string('lol')
print(stroka)
def is_palindrome( word='hello'):
    return word == word[::-1]

stroka = is_palindrome('lol')
print(stroka)



def calculator(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '//':
        return num1 // num2
    elif operator == '/':
        return num1 / num2
    elif operator == '**':
        return num1 ** num2
    elif operator == '%':
        return num1 % num2


result = calculator(12, '+', 34)
print(result)



