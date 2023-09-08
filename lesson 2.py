def get_zodiac_sign(day, month):
    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    else:
        return "Capricorn"

def validate_date(day, month):
    if month < 1 or month > 12:
        return False
    if month == 2:
        if day < 1 or day > 29:
            return False
    elif month in [4, 6, 9, 11]:
        if day < 1 or day > 30:
            return False
    else:
        if day < 1 or day > 31:
            return False
    return True

def main():
    while True:
        print("Введите день и месяц рождения (через пробел):")
        user_input = input()
        inputs = user_input.split()
        if len(inputs) != 2:
            print("Неверный ввод!")
            continue
        try:
            day = int(inputs[0])
            month = int(inputs[1])
        except ValueError:
            print("Неверный ввод!")
            continue
        if not validate_date(day, month):
            print("Неверная дата!")
            continue
        sign = get_zodiac_sign(day, month)
        print(f"Ваш знак зодиака: {sign}")
        break


