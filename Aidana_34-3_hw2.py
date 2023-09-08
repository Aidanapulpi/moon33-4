day = int(input('Введите день рождения'))
month = int(input('Введите месяц рождения'))

if (day>=21 and day<=31 and month == 3 or day>=1 and day<=20 and month == 4):
    print('Овен')
elif(day>= 21 and day<=30 and month==4 or day>=1 and day<=21 and month == 5):
    print('телец')
elif(day>=22 and day<=31 and month==5 or day>=1 and day<=21 and month==6):
    print('близнецы')
elif(day>=22 and day<=30 and month==6 or day>=1 and day<=22 and month==7):
    print('рак')
elif(day>=23 and day<=31 and month==7 or day>=1 and day<=21 and month==8):
   print('лев')
elif(day>=22 and day<=31 and month==8 or day>=1 and day<=23 and month==9):
    print('дева')
elif(day>=24 and day<=30 and month==9 or day>=1 and day<=23 and month==10):
    print('весы')
elif(day>=24 and day<=30 and month==10 or day>=1 and day<=22 and month==11):
    print('скорпион')
elif(day>=23 and day<=30 and month==11 or day>=1 and day<=22 and month==12):
    print('стрелец')
elif(day>=23 and day<=31 and month==12 or day>=1 and  day<=20 and month==1):
    print('козерог')
elif(day>=21 and day<=30 and month==1 or day>=1 and day<=19 and month==2):
    print('водолей')
elif(day>=20 and day<=31 and month==2 or day>=1 and day<=20 and month==3):
    print('рыбы')
else:
    print('Неправильный ввод \n'
          'Пример: Введите день рождения:23 \n'    
          'Введите месяц рождения7 ')