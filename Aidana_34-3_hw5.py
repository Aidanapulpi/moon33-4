Geeks = {
    'address': 'Toktogula 175',
    'courses': ['Android', 'Backend', 'Frontend'],
    'bag': {'fails', 'errors', 'stack'}
}
Geeks.pop('bag')
Geeks['address'] = 'Ibraimova 103'
Geeks['phone'] = '0507052018'
Geeks['instagram'] = "geeks_edu"
new_courses = ['UX/UI Дизайнер', 'PM']
Geeks['courses'].extend(new_courses)
Geeks['courses'] = set(Geeks['courses'])
Geeks['founding_date'] = '05.05.2018'
print(len(Geeks['courses']))

for key, value in Geeks.items():
    print(f'{key} : {value}')



