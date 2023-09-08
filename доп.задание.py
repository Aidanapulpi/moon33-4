search_ingridient = {
    'лагман': {'мясо', 'лапша', 'перец'},
    'борщ': {'свекла', 'морковь', 'капуста'},
    'пицца': {'колбаса','сыр','тесто'},
    'суши': {'рис', 'творожный сыр','рыба'},
    'манты': {'мясо', 'лук', 'тесто'}

}
while True:
    name = input('Введите ингридиент')
    found = False
    for key, value in search_ingridient.items():
        if name in value:
            print(key)
            found = True
    if found == False:
        print('Такого ингридиента нет! Введите другой')

menu = {  'laghman': {'meat', 'noodles', 'pepper'},
          'manti': {'meat', 'onion', 'dough'},
          'okroshka': {'kefir', 'radish', 'sausage'},
          'salad': {'tomat', 'cucumber', 'onion'} }
inverted_menu = dict()
for dish, ingridients in menu.items():
    for ingridient in ingridients:
        if ingridient in inverted_menu:    inverted_menu[ingridient].add(dish)
        else:    inverted_menu[ingridient] = {dish}
        while True:  query = input('enter ingridient: ').lower()
        if query == 'q':   break
result = inverted_menu.get(query)
print(result)