menu = {
    'lagman' : {'лапша', 'мясо', 'перец'},
    'manty': {'мясо', 'тесто', 'лук'},
    'okroshka': {'кефир', 'редиска', 'колбаса'},
    'свежий': {'томат', 'огурец', 'помидор'}
}

while True:
    name = input('enter name: ')
    if name in menu:
        print(menu[name])
    else:
        print(f'такого нет! maybe interest for you: {tuple(menu.keys())}')

        