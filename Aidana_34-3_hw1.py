monday = int(input('введите расход за понедельник'))
tuesday = int(input('введите расход за вторник'))
wednesday = int(input('введите расход за среду'))
thursday = int(input('введите расход за четверг'))
friday = int(input('введите расход за пятницу'))
saturday = int(input('введите расход за субботу'))
sunday = int(input('введите расход за воскресенье'))

sum_ras = monday + tuesday + wednesday + thursday + friday + saturday + sunday
print(f'Общая сумма {sum_ras}')

average = sum_ras
round_a = round(average, 1)
print(f'Средний расход {round_a}')



